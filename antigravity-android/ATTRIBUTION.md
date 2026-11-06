# Antigravity for Android — Attribution

This folder documents and links the open-source project used as the
mobile AI coding environment for Digital Products services.

- **Original project:** Antigravity for Android
- **Repository:** https://github.com/werdio325-png/antigravity-android
- **Author:** werdio325-png
- **License:** Apache License 2.0 (see LICENSE below in the original repo)
- **Version used:** 2.4.1 (checked 2026-11-06)
- **What it is:** A third-party (not Google official) standalone port of
  Google Antigravity that runs natively on Android ARM64 phones.
  Gemini-powered autonomous agentic coding: inspect repos, write code
  across files, compile, run tests — on-device, no computer needed.
- **Local copy (source subset, no 51 MB binary):** `~/workspace/agy-src`
  on the Muse VM — modules, app, web, config, docs, build.sh.
  The 51 MB `language_server.tar.gz` binary is NOT copied here;
  download it from the original repo's releases when building.

## Do NOT use
- The `antigravity-region-bypass.apk` variant — it bypasses Google's
  account eligibility checks. Use only the standard `antigravity.apk`.
- This is not a Google product. Do not present it to clients as Google's.

## How Digital Products uses it
- Phone-based AI coding environment for building client apps/websites.
- Works together with this repo (business-hub): Muse does outreach,
  planning and web work; Antigravity on Android builds code from the
  same GitHub repos.
