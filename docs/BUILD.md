# Build and publish — Yugatn Art

## Canonical source

**`index.html` on `main` is the single source of truth** for the running prototype. The project is currently a dependency-free, single-file browser app; there is no compile/bundle step.

| Artifact | Role |
|---|---|
| `index.html` | Canonical runtime application |
| `scripts/validate-prototype.py` | Shared static source-integrity checks used by CI and both publish workflows |
| `scripts/apply-v0.5.py` | Historical recovery tool only — do not run on every push |
| `payloads/*` | Archived payloads; not used for publishing |
| `scripts/deploy-index-v0.4.py` / `v0.5.py` | Deprecated helpers; do not use as the normal build path |

A previous v0.4 payload deployment overwrote lock/alphaLock behavior from commit `2aa99d8`; that behavior was restored in Prototype 0.5. Do not regenerate `index.html` from archived payloads unless recovering a known regression.

## Local run

```bash
python3 -m http.server 8080
# open http://127.0.0.1:8080/
```

## Validation boundary

`scripts/validate-prototype.py` checks HTML structure, duplicate IDs, required controls and version markers, labels, literal `getElementById` targets, and the single inline script. CI then runs `node --check` on that script.

These are **static checks only**. They do not prove that canvas drawing, pointer input, IndexedDB, file import/export, undo/redo, or stylus pressure works in a browser. Runtime tests must be recorded separately in `docs/TEST_LOG.md`.

## Workflows

| Workflow | Purpose |
|---|---|
| `Validate prototype source` | Shared structural checks + JavaScript syntax check |
| `Deploy static prototype to GitHub Pages` | Official Pages deployment; requires Pages enabled by repository owner |
| `Deploy static site to gh-pages branch` | Alternative branch deployment |

Both publishing workflows validate the canonical source before publishing. They construct a fresh `_site/` directory and publish an explicit allowlist containing only `index.html` and `.nojekyll`; repository docs, archived payloads, and workflow files are not included in the public site artifact.

## Enable GitHub Pages (owner, one-time)

**Option A — GitHub Actions**

1. Open repository **Settings → Pages**.
2. Under **Build and deployment → Source**, choose **GitHub Actions**.
3. Re-run workflow **Deploy static prototype to GitHub Pages** (Actions → workflow → Run workflow).
4. Confirm `https://yugatn.github.io/yugatn_art/` returns HTTP 200 and contains the Prototype 0.5 UI.

**Option B — branch `gh-pages`**

1. Ensure workflow **Deploy static site to gh-pages branch** succeeds.
2. Set Source to **Deploy from a branch**, branch `gh-pages`, folder `/(root)`.
3. Wait for Pages to finish publishing, then check the same URL.

If `actions/configure-pages` fails with `Resource not accessible by integration` or site Not Found, record the failing step and response. The workflow token cannot necessarily create/enable the Pages site; an owner-side Settings action is required.

## Publish guard

The shared validator rejects missing version markers, required controls, duplicate IDs, unresolved literal DOM hooks, missing document metadata, and unexpected script structure before deployment.
