#!/usr/bin/env python3
"""Validate the static site; --release additionally rejects unfinished policies."""
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent
errors = []
release = '--release' in sys.argv

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.headings = 0
        self.main = 0
        self.lang = False
        self.viewport = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'h1': self.headings += 1
        if tag == 'main': self.main += 1
        if tag == 'html': self.lang = attrs.get('lang') == 'en'
        if tag == 'meta' and attrs.get('name') == 'viewport': self.viewport = True
        if tag in ('script', 'iframe', 'form'):
            errors.append(f'{self.path}: unexpected {tag}')
        for key in ('href', 'src'):
            target = attrs.get(key)
            if not target or target.startswith('#'): continue
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                if tag != 'a': errors.append(f'{self.path}: external asset {target}')
                if parsed.scheme not in ('https', 'mailto'): errors.append(f'{self.path}: unsafe link {target}')
                continue
            resolved = (self.path.parent / unquote(parsed.path)).resolve()
            if resolved.is_dir(): resolved /= 'index.html'
            if not resolved.is_relative_to(ROOT) or not resolved.exists():
                errors.append(f'{self.path}: broken relative link {target}')

for path in ROOT.rglob('*.html'):
    source = path.read_text()
    page = Page(path)
    page.feed(source)
    if page.headings != 1 or page.main != 1 or not page.lang or not page.viewport:
        errors.append(f'{path}: missing semantic page structure')
    if release:
        if re.search(r'\[[A-Z][^\]]*\]', source) or 'class="draft"' in source or 'not yet effective' in source:
            errors.append(f'{path}: unresolved draft or placeholder')
        if 'name="robots" content="noindex"' in source:
            errors.append(f'{path}: remove draft noindex metadata before publication')
if release:
    manifest = json.loads((ROOT / 'release.json').read_text())
    if manifest.get('approved') is not True or not all(v is True for v in manifest['checks'].values()):
        errors.append('release.json: publication review incomplete')
    if not (ROOT / 'archive' / manifest['version'] / 'privacy' / 'index.html').exists() or not (ROOT / 'archive' / manifest['version'] / 'terms' / 'index.html').exists():
        errors.append('Archive the approved policy version before release')
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print('Release checks passed.' if release else 'Static site checks passed (draft mode).')
