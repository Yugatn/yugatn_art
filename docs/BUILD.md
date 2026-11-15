# Build and publish — Yugatn Art

## Canonical source

**`index.html` on `main` is the single source of truth** for the running prototype.

| Artifact | Role |
|---|---|
| `index.html` | Canonical application (edit this file) |
| `scripts/apply-v0.5.py` | Historical recovery tool only — do not run on every push |
| `payloads/*` | Archived multi-part payloads; not used for publish |
| `scripts/deploy-index-v0.4.py` / `v0.5.py` | Deprecated publish helpers |

Do not regenerate `index.html` from payloads unless recovering from a known regression. A previous v0.4 payload deploy overwrote lock/alphaLock features from commit `2aa99d8`; that was restored in prototype 0.5.

## Local run

```bash
# any static server, or open the file directly
python3 -m http.server 8080
# open http://127.0.0.1:8080/
```

## Continuous integration

| Workflow | Purpose |
|---|---|
| `Validate prototype source` | `node --check` on extracted JS + required 0.5 DOM/markers |
| `Deploy static prototype to GitHub Pages` | Official Pages (needs Settings enable once) |
| `Deploy static site to gh-pages branch` | Publishes `_site/` to branch `gh-pages` |

Validate runs on every push and PR. It fails if Prototype 0.5 markers or layer controls are missing.

## Enable GitHub Pages (owner, one-time)

**Option A — GitHub Actions (preferred)**

1. Open repository **Settings → Pages**.
2. Under **Build and deployment → Source**, choose **GitHub Actions**.
3. Re-run workflow **Deploy static prototype to GitHub Pages** (Actions → workflow → Run workflow).
4. Confirm `https://yugatn.github.io/yugatn_art/` returns HTTP 200 and shows Prototype 0.5.

**Option B — Branch `gh-pages`**

1. Ensure workflow **Deploy static site to gh-pages branch** has completed successfully (creates/updates branch `gh-pages`).
2. Settings → Pages → Source = **Deploy from a branch** → Branch **gh-pages** / **/ (root)**.
3. Wait for the Pages build, then open the same URL.

Without one of these owner steps, Pages remains **BLOCKED**: `actions/configure-pages` cannot create the site (`Resource not accessible by integration`).

## Version guard

Publish workflows refuse to deploy if `index.html` lacks:

- `Prototype 0.5`
- `stabStep`
- `alphaLock`
- `duplicateLayer`
