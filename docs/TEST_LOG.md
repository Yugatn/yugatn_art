# Test log — Yugatn Art

**Last code update reviewed:** 2026-10-10  
**Test execution status:** NOT RUN in a real browser or stylus device during this implementation pass. No pass is claimed.

## Repository observations

- Default branch: `main`.
- A GitHub Pages workflow exists at `.github/workflows/pages.yml` and is triggered by pushes to `main`/ `master` or manual dispatch.
- The repository owner reported that the Pages URL currently returns 404. The workflow file alone does not prove that Pages is configured or that a deployment succeeded.
- Check **Settings → Pages** and **Actions → Deploy static prototype to GitHub Pages**. If Pages is not enabled, select GitHub Actions as the build/deployment source and rerun the workflow.
- The current repository prototype is a single `index.html`; modularization remains pending.

## Features implemented in code, awaiting execution

- Editable project save/open using version-1 `.yugatn` JSON with base64 PNG data per layer.
- Debounced local autosave in IndexedDB and startup attempt to restore the last saved draft.
- Canvas zoom via wheel, pan via Space+drag, and fit/reset.
- Pressure response curve control for pointer pressure reported by a stylus.
- Autosave hooks for strokes and common layer/settings changes.
- A four-entry pixel-snapshot undo history limit.

## Test results

| Test | Result | Evidence |
|---|---|---|
| Static source update present on `main` | OBSERVED | GitHub contents API returned the updated `index.html` after commits |
| Browser syntax/runtime | NOT RUN | No browser execution available in this pass |
| Chrome/Safari/Firefox drawing | NOT RUN | No browser/device test log supplied |
| `.yugatn` round-trip | NOT RUN | Manual checklist pending |
| IndexedDB reload recovery | NOT RUN | Manual checklist pending |
| Zoom/pan interactions | NOT RUN | Manual checklist pending |
| Real stylus pressure | NOT TESTED | Requires supported physical stylus/browser |
| GitHub Pages deployment | NOT VERIFIED | Owner-reported 404; deployment/configuration not confirmed |

## Next test pass

Run every applicable item in `docs/TESTING.md`, record browser and OS versions, and attach reproducible defects before marking a feature complete.