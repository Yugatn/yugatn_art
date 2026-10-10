# Test log — Yugatn Art

**Last code update reviewed:** 2026-10-10 (Stage A)  
**HEAD at log write:** see latest `main` after Stage A docs/CI commits.

## Stage A — repository observations (OBSERVED)

| Check | Result | Evidence |
|---|---|---|
| Default branch | `main` | clone / API |
| `index.html` reports Prototype 0.5 | OBSERVED | markers: `Prototype 0.5`, `stabStep`, `alphaLock`, `locked`, `duplicateLayer`, `layerThumbData`, `source-atop` |
| Inline JS syntax | PASS (static) | `node --check` on extracted script locally and via Validate workflow |
| Validate workflow | expected PASS after Stage A push | `.github/workflows/validate.yml` extended with 0.5 markers |
| Official Pages deploy | FAIL / BLOCKED | Job fails at **Configure Pages**; site API not found; token cannot create Pages site |
| Public URL | FAIL | `https://yugatn.github.io/yugatn_art/` → HTTP **404** |
| `gh-pages` branch deploy | added in Stage A | workflow `deploy-gh-pages-branch.yml`; result after first run |
| Browser UI / drawing | NOT_TESTED | no interactive browser in this agent environment |
| Real stylus pressure | NOT_TESTED | needs physical device |
| `.yugatn` pixel round-trip | NOT_TESTED | Stage B |
| IndexedDB autosave reload | NOT_TESTED | Stage B |

### Pages failure detail (OBSERVED)

- Workflow: `Deploy static prototype to GitHub Pages`
- Failing step: **Configure Pages** (`actions/configure-pages`)
- Subsequent steps (Upload, Deploy) are skipped
- Root cause class: repository Pages product not enabled for GitHub Actions source; workflow token lacks permission to create the site (`Resource not accessible by integration` / site Not Found)
- **Owner action required:** Settings → Pages → Source = GitHub Actions **or** Deploy from branch `gh-pages` (see `docs/BUILD.md`)

## Features present in source (code review, not runtime PASS)

- Brush / eraser / line / eyedropper
- Streamline stabilizer (`stabStep` / `stabFlush`)
- Layers: opacity, blend modes, lock, alpha lock (`source-atop`), duplicate, reorder, solo, thumbnails
- Undo/redo: pixel snapshots, history length 4 (structural layer ops not fully command-based)
- `.yugatn` v1 JSON + base64 PNG per layer
- IndexedDB debounced autosave
- Zoom (wheel), pan (Space+drag), fit

## Next passes

1. Owner enables Pages (A or B in `docs/BUILD.md`) → re-check HTTP 200 + Prototype 0.5 in page source.
2. Stage B: automated functional tests (layers, draw, history bounds, import validation).
3. Manual browser matrix per `docs/TESTING.md`.
