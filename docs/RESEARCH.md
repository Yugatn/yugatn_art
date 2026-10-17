# Public-source research notes

**Research pass:** 2026-10-10  
**Purpose:** translate established digital-art workflows into product requirements, not reproduce proprietary implementations.

## Procreate

Official handbook:
- Brushes: https://help.procreate.com/procreate/handbook/brushes
- Brush Studio settings: https://help.procreate.com/procreate/handbook/brushes/brush-studio-settings
- Apple Pencil behavior: https://help.procreate.com/procreate/handbook/5.2/interface-gestures/pencil
- Stylus preferences and pressure curve: https://help.procreate.com/procreate/handbook/5.1/actions/actions-preferences

Observed product patterns:
- Distinct paint, smudge, and erase workflows can share a brush library.
- Brush behavior can be customized through stroke path, spacing, smoothing, shape/grain, pressure, tilt, opacity, flow, and related parameters.
- Pen input should influence the mark rather than merely act as a mouse substitute.
- The application should expose pressure response in a way artists can tune.

Implications for Yugatn Art:
- Use a normalized input event model and keep brush parameters independent of UI controls.
- Add pressure curves, tilt response, taper and texture in stages.
- Keep a fast, discoverable path for selecting brush, eraser, color and size.

## ibis Paint X

Official sources:
- Product overview: https://ibispaint.com/about.jsp?lang=en-US
- Official welcome/features page: https://ibispaint.com/greeting/
- Official tutorial index: https://ibispaint.com/lecture/index.jsp?lang=en&no=0
- Layers: https://ibispaint.com/lecture/index.jsp?lang=en&no=06
- Clipping: https://ibispaint.com/lecture/index.jsp?lang=en-US&no=30
- Manga tools: https://ibispaint.com/lecture/index.jsp?no=185
- Recent feature notes: https://ibispaint.com/newFeature.jsp?lang=en%23ver90400

Observed product patterns:
- The product emphasizes a large brush/material library and frequent illustration-specific tools.
- The official tutorials document layer ordering, visibility, opacity, clipping, import/trace workflows, selection, fill, rulers, manga frames and screen tones.
- Stabilization and line rendering are actively developed features.
- Timelapse and sharing/community workflows are part of the product's wider ecosystem.

Implications for Yugatn Art:
- Treat line stabilization as a core drawing feature rather than a decorative slider.
- Prioritize clipping, symmetry/rulers, fill, selection, reference-image import, and line-art workflows after the drawing foundation.
- Add timelapse/community capabilities only after privacy, storage, moderation, and performance have been designed.

## Adobe Photoshop

Official painting-tools guide:
- https://helpx.adobe.com/photoshop/using/painting-tools.html

Observed product patterns:
- Brush and pencil tools coexist with eraser, blur and smudge tools.
- Brush presets and configurable tip behavior are important to repeatable workflows.
- Opacity and flow are separate controls.
- Tablet pressure, angle, rotation and stylus wheel can affect brush behavior.
- Texture and blending behavior support image finishing as well as drawing.

Implications for Yugatn Art:
- Do not collapse opacity and flow into one parameter.
- Establish a layer compositing model and a test suite for blend modes.
- Build reversible image adjustments, masks, selections and transforms before claiming professional editing parity.

## Cross-product synthesis

| Area | Product lesson | Yugatn Art direction |
|---|---|---|
| Drawing feel | Input should feel immediate and expressive | Low-latency stroke pipeline with pressure-aware brush dynamics |
| Stabilization | Clean linework needs explicit controls | Adjustable stabilization, sampling and taper |
| Layers | Illustration work relies on separated elements | Reorder, groups, visibility, opacity, blend modes, clipping and masks |
| Brushes | Presets plus customization serve different skill levels | Useful defaults first; advanced brush editor later |
| Manga/line art | Rulers, frames, tones and fill can accelerate specialized work | Add symmetry, rulers, fill and manga helpers as a focused feature set |
| Editing | Paint tools and compositing need to coexist | Non-destructive adjustments and selection/transform tools |
| Input access | Not all artists have a pressure stylus | Mouse/touch fallback remains fully usable |
| Reliability | Complex artwork needs predictable recovery | Native project format, autosave, crash recovery, versioned history |

## Evidence and limitations

This is a first-pass desk review of official public materials, not a hands-on benchmark or a complete competitive audit. Feature availability can vary by operating system, version, device and subscription. No claims are made about comparative performance, exact brush counts, file-format compatibility or implementation internals. Those require current version checks and reproducible testing.

The application should be judged against original acceptance criteria and artist testing, not a checklist that merely mirrors competitor feature counts.
