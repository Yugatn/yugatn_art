# Testing checklist — Yugatn Art

**Status:** checklist prepared; browser/device execution has not yet been confirmed.

## Basic drawing
- [ ] Open `index.html` or the GitHub Pages deployment in a current browser.
- [ ] Draw several separate strokes with mouse/trackpad.
- [ ] Test brush size and opacity changes.
- [ ] Test eraser and straight-line tool.
- [ ] Test eyedropper against a known color.
- [ ] Test undo/redo after multiple strokes.
- [ ] Confirm that changing the selected layer changes where new marks are drawn.

## Layers and export
- [ ] Add two layers and draw visibly different marks on each.
- [ ] Hide a layer and confirm it is absent from PNG export.
- [ ] Change layer opacity and blend mode; compare canvas preview and exported PNG.
- [ ] Clear a layer and confirm undo restores the cleared pixels.
- [ ] Export a PNG and verify dimensions are 1400 × 900 px.
- [ ] Toggle transparent paper, export, and verify the PNG alpha channel in an image viewer.

## Editable project round-trip
- [ ] Draw on at least two layers and rename one.
- [ ] Change visibility, opacity, blend mode and brush settings.
- [ ] Save as a `.yugatn` file.
- [ ] Start a new artwork, then reopen the saved file.
- [ ] Verify pixels, layer order, layer names, visibility, opacity, blend mode and document name.
- [ ] Open an invalid JSON file and confirm the app reports an error without replacing the current artwork.
- [ ] Test a project over the 150 MB file limit.
- [ ] Verify that a project with unsupported dimensions is rejected.

## Device and responsive checks
- [ ] Desktop Chrome: mouse drawing, keyboard shortcuts and file dialogs.
- [ ] Desktop Safari and Firefox: canvas pointer capture and file import/export.
- [ ] Tablet with a supported stylus: confirm whether real pressure values are reported.
- [ ] Touch-only device: verify that drawing is possible and accidental page scrolling is controlled.
- [ ] Narrow viewport: ensure core canvas and tool rail remain usable.
- [ ] Large/long drawing session: observe memory consumption and undo behavior.

## Known test limitations
- The project currently uses full-canvas pixel snapshots for undo. History is capped to four snapshots to reduce memory use; this is a temporary tradeoff, not a scalable production history system.
- The project file is JSON containing base64 PNG images per layer. This is simple but increases file size; a binary/ZIP-based format should be designed before large-canvas support.
- Autosave, crash recovery, drag-to-reorder layers, canvas zoom/pan/rotation, and a complete stylus pressure curve are not implemented yet.
- No browser/device test result should be considered passed until it is executed and recorded with browser/device details.
