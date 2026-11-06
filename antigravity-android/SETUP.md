# Antigravity for Android — Phone Setup Guide

## 1. Download
- Open https://github.com/werdio325-png/antigravity-android/releases
- Download **antigravity.apk** ONLY (standard release).
- Do NOT download `antigravity-region-bypass.apk`.

## 2. Install
- Allow "Install unknown apps" for your browser/file manager.
- Install the APK.
- Grant **All Files Access** (Storage permission).

## 3. Install runtimes
Open the in-app terminal and run:
```
pkg update && pkg install git python nodejs
```

## 4. (Optional) Shizuku for ADB-level access
- Install Shizuku from Google Play, start it via wireless debugging.
- Antigravity can then do package installs and system diagnostics
  without root.

## 5. Open a repo and build
- Clone your repo (e.g. business-hub) inside the app.
- Ask the agent, e.g. "Add a booking form page to this Flask app".
- The agent edits files, runs builds and fixes errors on-device.

## 6. Work with Muse
- Muse (this assistant) does client outreach, planning and web work
  on the same GitHub repos.
- Antigravity on your phone builds the code.
- Both push to the same repo — no duplicate work.

## Troubleshooting
- App won't start: check ARM64 (Settings > About phone > processor).
- Agent can't reach GitHub: check `git` is installed via `pkg`.
- Region error on sign-in: use a Google account in a supported
  region; do NOT use the bypass APK.
