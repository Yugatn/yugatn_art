# Product specification — Yugatn Art

**Version:** 0.1 draft  
**Status:** workflow prototype; production drawing engine not yet implemented.

## 1. Product goal

Build a comfortable digital art application for illustration, sketching, painting, inking, and image finishing. The app should feel approachable on first use while retaining a path to professional workflows.

This is an independent product. It must not copy proprietary source code, brushes, assets, branding, or distinctive UI from other applications.

## 2. Product principles

1. **Canvas first.** Keep the drawing surface dominant and tools close to the hand.
2. **Stylus is an enhancement, not a requirement.** Mouse, trackpad, touch, and supported pen input must all be usable.
3. **Non-destructive by default.** Prefer layers, masks, reversible adjustments, and a clear undo history.
4. **Progressive complexity.** Essential tools stay visible; advanced controls appear when needed.
5. **Reliable documents.** Autosave, crash recovery, predictable exports, and clear file formats are core functionality, not optional polish.
6. **Performance is a feature.** Low-latency strokes and predictable memory usage must be measured on representative hardware.
7. **Accessible interaction.** Keyboard shortcuts, clear focus states, readable labels, and adjustable UI density.
8. **Honest AI.** AI-assisted tools must be opt-in, identify generated/modified content, and never overwrite artwork without explicit acceptance.

## 3. Reference products and transferable lessons

### Procreate
Study direct manipulation, pressure/tilt-aware brushes, brush customization, quick tool switching, and the canvas-first experience.

Official references:
- https://help.procreate.com/procreate/handbook/brushes
- https://help.procreate.com/procreate/handbook/brushes/brush-studio-settings
- https://help.procreate.com/procreate/handbook/5.2/interface-gestures/pencil

### Adobe Photoshop
Study brush presets, painting and erasing tools, opacity/flow separation, tablet input, blending, and mature compositing workflows.

Official reference:
- https://helpx.adobe.com/photoshop/using/painting-tools.html

### ibis Paint X
Research areas for a dedicated verification pass: stabilization, rulers and symmetry, clipping layers, manga/illustration workflow, reference windows, brush catalog, timelapse, and community/export features. Verify each feature against current official ibis Paint materials before turning it into a compatibility or parity claim.

## 4. Target users

- Beginners who need to open the app and draw immediately.
- Digital illustrators and concept artists who use a pen display or tablet.
- Manga, comic, and line-art creators.
- Artists who combine hand drawing with image editing and compositing.
- Mouse/trackpad users who do not own a stylus.
- Creators who want a portable project file and dependable image export.

## 5. MVP scope

### Included in the browser prototype
- Responsive dark workspace.
- Pointer-based freehand strokes.
- Brush size, opacity, color, and basic line stabilization.
- Eraser, straight-line tool, and eyedropper.
- Basic layer stack: add, select, rename, delete, visibility, opacity, blend mode.
- Undo/redo for layer pixel edits.
- PNG export.
- Keyboard shortcuts for core tools.
- No external runtime dependencies.

### Required before calling the product a usable MVP
- Reliable undo/redo covering every document operation.
- Persistent local project saving and recovery.
- Explicit document dimensions, DPI metadata strategy, and transparent-background export.
- Proper line rendering with interpolation, pressure curves, and configurable stabilization.
- Layer thumbnails and drag-to-reorder.
- Zoom/pan/rotate canvas, fit-to-screen, and pixel-accurate navigation.
- Robust touch-vs-draw gesture handling and palm rejection where the platform permits it.
- Automated tests for document state, history, rendering, and export.
- Accessibility and keyboard navigation review.

## 6. Drawing and input architecture

Keep these responsibilities separate:

- **Input adapters:** Pointer Events, platform stylus APIs, touch, mouse, trackpad.
- **Input normalization:** coordinates, pressure, tilt, azimuth, timestamp, pointer identity, contact state.
- **Stroke processor:** filtering, stabilization, resampling, smoothing, tapering.
- **Brush engine:** tip shape, spacing, opacity, flow, texture, blend behavior, pressure/tilt response.
- **Raster renderer:** paint, erase, smudge, masks, compositing, GPU acceleration when justified.
- **Document model:** canvas dimensions, color profile, layers, masks, visibility, blend mode, metadata.
- **History engine:** reversible commands, checkpoints, bounded memory, crash-safe recovery.
- **Persistence:** versioned native project format, autosave, import/export.
- **UI:** tool selection, contextual inspector, shortcuts, panels and workspace layouts.

Do not bake device-specific behavior into the brush renderer. The renderer should consume normalized input so it can be tested independently.

## 7. Input fallback behavior

- Stylus with pressure: map pressure through a configurable response curve.
- Stylus without pressure: use stable fixed-width strokes and retain all other tools.
- Mouse/trackpad: use predictable constant pressure; optional simulated taper may be enabled by the user.
- Touch: support drawing, but avoid accidental canvas gestures by providing configurable modes and clear palm/touch behavior.
- Missing tilt/azimuth: ignore those parameters gracefully.
- Unsupported browser or hardware feature: explain the limitation without blocking drawing.

Do not claim pressure sensitivity merely because Pointer Events expose a pressure field; verify the actual hardware/browser reports useful values.

## 8. Document model and file formats

Initial direction:
- Native project: versioned archive containing a manifest, layer data, thumbnails, and optional recovery journal.
- PNG: first raster export target, including alpha.
- JPEG: later export for flattened images.
- PSD interoperability: investigate separately; do not promise full PSD fidelity without a tested specification and compatibility suite.
- SVG: useful for vector tools or shapes, but not a replacement for a raster painting document.

Store canvas dimensions, color-space intent, layer ordering, opacity, visibility, blend mode, and application version in the project manifest. Validate all imported metadata and limit decompression/memory use for untrusted files.

## 9. UX layout

- **Top bar:** document name, undo/redo, file actions, export.
- **Tool rail:** brush, eraser, line/shape, selection, fill, transform, eyedropper.
- **Canvas center:** dominant, pannable/zoomable surface with optional transparent checkerboard.
- **Inspector:** context-sensitive brush settings, color controls, layers and blend modes.
- **Mobile/tablet:** collapsible panels, large hit targets, optional gesture shortcuts, no required hover interactions.
- **Desktop:** keyboard shortcuts, dockable panels, mouse-friendly controls, optional compact mode.

## 10. Later capabilities

- Brush editor with tip shape, texture/grain, spacing, dynamics, pressure curves, tilt response, taper and stabilization.
- Selection tools, lasso, transform, crop, fill, gradients, shapes and text.
- Clipping masks, alpha lock, layer masks, groups, reference image, symmetry and perspective rulers.
- Color management and adjustment layers.
- Animation/timelapse.
- Brush import/export after format and security review.
- Optional AI assistance: reference exploration, ideation, selection assistance, local or remote generation, and non-destructive variations. AI is not required for core drawing and must never silently replace a layer.

## 11. Non-functional requirements

- No silent data loss; autosave and recovery are required for production use.
- Smooth drawing at the target display refresh rate on agreed baseline hardware.
- Large canvases must be tiled or otherwise memory-managed rather than relying on unlimited full-resolution snapshots.
- Native project format must be versioned and migration-tested.
- Importers must validate dimensions and resource limits.
- Core drawing should work offline.
- Optional cloud/AI services must be clearly disclosed and separately configurable.

## 12. Acceptance criteria for MVP

1. A new user can open the app and draw without an account or stylus.
2. Mouse, touch, and stylus-capable input paths are tested separately.
3. Undo and redo reproduce the prior document state exactly.
4. Hidden layers do not appear in exports.
5. PNG export preserves the intended transparency and dimensions.
6. A saved project reopens with its layer order and settings intact.
7. A failed save or interrupted session has a documented recovery path.
8. Core interactions work at desktop and tablet viewport sizes.
