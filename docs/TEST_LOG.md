# Test log — Yugatn Art

**Last code update reviewed:** 2026-10-10 (Stage A hardening branch)  
**Runtime status:** no browser/device PASS is inferred from static CI.

## Stage A — repository observations

| Check | Result | Evidence |
|---|---|---|
| Canonical runtime source | OBSERVED | `index.html` on `main` |
| Prototype 0.5 markers and controls | OBSERVED | `index.html` |
| Existing static syntax check | PASS (reported) | `node --check` on extracted inline JS |
| Official Pages deployment | BLOCKED (reported) | `Configure Pages` failure; owner must enable Pages/source |
| Public demo URL | FAIL (reported) | `https://yugatn.github.io/yugatn_art/` returned HTTP 404 in Stage A report |
| Branch deployment | PASS (reported) | `gh-pages` workflow succeeded |
| Browser UI / drawing | NOT_TESTED | Requires browser execution |
| Real stylus pressure | NOT_TESTED | Requires supported physical device |
| `.yugatn` pixel round-trip | NOT_TESTED | Requires functional test |
| IndexedDB reload recovery | NOT_TESTED | Requires browser execution |

## Stage A hardening — implementation intent

The hardening branch adds a shared static validator, checks literal DOM references and duplicate IDs, and makes both deploy workflows publish an allowlisted directory containing only `index.html` and `.nojekyll`.

**Status until workflows run on this branch:** NOT_TESTED. Do not label these checks PASS until GitHub Actions confirms success.

## Stage B — next runtime checks

1. Verify the live demo returns HTTP 200 and contains Prototype 0.5.
2. Add automated browser smoke tests for startup, drawing, layers, undo/redo, save/open and autosave.
3. Record actual browser/OS/version and each test result; keep stylus hardware testing separate.
