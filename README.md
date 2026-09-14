# Lumi Hair legal site

This README is authoritative for editing, review, and publication of this repository. The HTML files are draft policy content, not effective agreements. The app repository's FEATURE.md remains authoritative for supported app behavior.

## Preview and check

Use Python 3.10 or newer. No JavaScript, build dependencies, third-party fonts, analytics, or forms are served.

```sh
python3 check.py
python3 -m http.server 8088 --bind 127.0.0.1
```

Open http://127.0.0.1:8088/. Check mobile and desktop widths, light/dark appearance, keyboard focus, zoom, and every navigation link. The mail link intentionally contains a placeholder until a monitored support address is provided.

## Required publication review

Do not enable GitHub Pages or push draft content to a publishing branch. Complete every field and review in release.json, then remove the draft banners and noindex metadata. Never put private customer information, credentials, or support requests in this repository.

- Supply the legal operator, mailing address, public support email, governing state, and effective date consistently. Replace the deletion mailto address as well as visible text.
- Verify actual Supabase hosting regions, backups, auth/security logs, and deletion schedules. Verify OpenAI model/account data controls, training opt-in settings, image safety retention exceptions, and processing regions. Do not promise zero retention without verification.
- Verify RevenueCat identifiers, diagnostics, transaction retention, and customer deletion handling. The current app deletes Supabase data; it does not automatically erase RevenueCat/store records or cancel subscriptions.
- Establish a monitored deletion mailbox. Verify ownership using the account's email or another appropriate recovery process; never ask for passwords. Track requests privately, apply relevant deadlines, delete through the trusted account-deletion workflow, address provider records/exceptions, and confirm completion. Document the actual handling period before publishing.
- Review advertising, sale/sharing, tracking and face-processing practices and applicable US state privacy obligations. Do not infer an absence of biometric processing from the lack of face authentication.
- Verify production AI behavior and actual Lumi+ benefits, subscription pricing/period/renewal disclosures, purchase, restore, cancellation, refunds, and store privacy declarations. These features remain In Progress in the app inventory.
- Obtain review of the final policies. The initial Terms intentionally omit arbitration, class-action waivers, and an invented liability cap.

## Archive and versions

Before publishing, copy the approved Privacy Policy and Terms into archive/2026-09-13/privacy/index.html and archive/2026-09-13/terms/index.html. Adjust relative root links to ../../../ and add links on archive/index.html. Preserve these copies on future changes. Archive only approved policies; do not represent the present drafts as previously effective policies.

For material updates, choose a new version consistently across release.json, the displayed HTML versions, app src/config/legal.ts, and a new database migration updating record_legal_acceptance and claim_hairstyle_preview_generation. Preserve old acceptance rows and archived documents. The app requires acceptance of the current terms/privacy version; AI disclosure approval applies separately to each new generation.

## Publish to GitHub Pages

Target repository: PacaiTEAM/lumi-hair-legal. Drafts are kept on `draft/legal-review`; no `main` publishing branch is created until approval. Create `main` from the reviewed draft when ready. Run this gate before committing an approved release:

```sh
python3 check.py --release
```

Once it passes, commit approved content to main and push. In GitHub choose Settings → Pages → Deploy from a branch → main → /(root). Enable/verify HTTPS. Expected base URL: https://pacaiteam.github.io/lumi-hair-legal/ (confirm the actual URL if the organization has a custom domain). The site uses relative links and supports the project subpath.

Use /privacy/, /terms/, and /delete-account/ URLs in store metadata. Configure Privacy Policy and Terms links in the RevenueCat dashboard paywall footer as well as the app-owned footer. Verify both Expo Go and native paywall presentation.

Keep Pages disabled while placeholders remain. The branch-based Pages publisher itself does not run check.py: an operator must pass the release check before every publishing push. For a future enforced deployment gate, switch to a GitHub Actions publishing workflow rather than branch publishing.

After HTTPS checks and deployment of the app's database migration and generation Edge Function, set EXPO_PUBLIC_LEGAL_PUBLISHED=true in app build configuration. Rebuild the app; the default is false to prevent acceptance of unfinished drafts. This flag is a client release guard, not a security authorization mechanism. Never enable it against unpublished URLs. Configure US availability and an 18+ audience consistently in store settings; the app records age attestation, not identity verification.

## Sources

- [GitHub Pages setup](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)
- [GitHub Pages IP logging](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)
- [OpenAI data controls](https://developers.openai.com/api/docs/guides/your-data)
- [Apple App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)
- [Google Play deletion requirements](https://support.google.com/googleplay/android-developer/answer/13327111?hl=en)
