# Prompt Patterns

Use these patterns as starting points. Keep the user's real domain, audience, and constraints. Replace bracketed fields.

## 0. Scope-Calibrated Design Exploration

Use when the user wants ideation but the level of focus could be whole product, feature, or narrow UX problem.

```text
Use case: ui-mockup
Asset type: scope-calibrated UI/UX exploration
Scope: [whole site/app | multi-screen product concept | specific feature | narrow design problem]
Primary request: Generate divergent design directions for [product/problem] at this exact scope. Use image generation as an inspiration channel, not a final source of truth.
Audience: [target user]
User job: [task, decision, or friction being solved]
Composition: [concept board | screen set | feature comparison | problem-solution board]
Required variety: each option must differ by product structure, interaction model, layout strategy, or problem-solving pattern.
Must include: primary object, user action, evidence/context, state change, and visible tradeoff.
Constraints: [brand, device, density, accessibility, existing product constraints]
Avoid: redesigning outside the selected scope, fake generated facts, cosmetic-only variations, generic dashboards, and irrelevant features.
Output goal: collect useful ideas, patterns, palette/layout signals, big directional moves, and failure signals that should sharpen the next prompt's avoid-list.
```

## 1. Divergent Interaction Models

Use when the user has an opportunity or UX problem but no settled product shape.

```text
Use case: ui-mockup
Asset type: UI/UX brainstorming contact sheet
Primary request: Create [4/6/8] radically different product concepts for [product/problem]. Do not make visual skins of the same dashboard; make different interaction models.
Audience: [target user]
User job: [decision/action]
Composition: one image containing a [2x2/3x2/4x2] grid of labeled UI concept thumbnails.
Required variety: [radar, queue, dossier, map, timeline, canvas, wizard, simulator, memo, scorecard, etc.]
Must include: primary object, core action, supporting evidence, and state.
Constraints: [domain tone, viewport, density, brand, accessibility]
Avoid: generic dashboards, vague AI panels, decorative art, repeated card layouts.
Output goal: maximize divergent thinking, expose surprising feature ideas, and reveal what directions should be rejected before convergence.
```

Useful instruction: "Each concept must differ by primary object and user loop, not only palette or component styling."

After each board, ask: "What worked, what failed, what felt generic or off-brand, and what should the next prompt explicitly avoid?"

## 2. Product-Led Growth Feature Invention

Use when the user asks "what should we build?" or wants a feature idea.

```text
Use case: ui-mockup
Asset type: product-led growth concept exploration
Primary request: Invent and visualize [4] product-led growth feature ideas for [business]. Start from the business opportunity, not from a prewritten feature list.
Audience: [growth team/user segment]
Composition: one [2x2] concept board. Each quadrant should show a different feature idea as a real screen, with a short name and the user loop implied by the UI.
Required variety: include one viral/share loop, one collaborative workflow loop, one trust/data-quality loop, and one quick utility loop.
Avoid: generic dashboards, vague AI copilots, fake marketing landing pages.
Output goal: use image generation to invent product ideas, not just make UI prettier.
```

Critique the result by asking: "What loop would cause a user to return, share, invite, or trust this?"

## 3. Mobile Constraint Solving

Use when the open question is information architecture under a tight viewport.

```text
Use case: ui-mockup
Asset type: mobile UX constraint exploration
Primary request: Show [4] different ways to solve the same problem on a narrow mobile screen: [mobile user job].
Audience: [mobile context]
Composition: [4] phone-sized screens side by side, each labeled with an interaction model.
Required patterns: [decision card stack, timeline story, scorecard with evidence drawer, chat-guided review, map, checklist, etc.]
Must include: [key entity], [fit/relevance signal], [evidence], [risk], primary action, secondary action.
Constraints: large touch targets, compact legible type, no tiny tables.
Avoid: desktop dashboard squeezed into mobile.
Output goal: compare mobile-first information architecture patterns.
```

Good mobile boards make the tradeoff visible: what gets promoted, collapsed, or deferred.

## 4. Visual System Tiles

Use when the question is color, typography, density, mood, or brand fit.

```text
Use case: ui-mockup
Asset type: visual direction and palette exploration
Primary request: Generate [6] distinct visual systems for the same [product/screen], focusing on color palette, typography mood, density, and hierarchy.
Composition: a [3x2] grid of UI style tiles. Each tile should include a small mockup, palette swatches, type label, and one-word mood.
Required moods: [list concrete moods]
Constraints: [brand/audience/domain]
Avoid: one-note palettes, generic gradients, repeated SaaS templates, rounded pill overload.
Output goal: choose visual direction quickly before implementing design tokens.
```

Ask for "mini UI plus swatches" instead of palette swatches alone. The same color behaves differently at product density.

## 5. Critique Redline

Use on an existing screenshot, generated mockup, or recreated flawed screen.

```text
Use case: ui-mockup
Asset type: critique annotation mockup
Primary request: Annotate this [screen/screenshot] with UX critique callouts directly on the image. The callouts should point to actual parts of the UI and explain what is wrong and how to improve it.
Composition: one app screenshot with visible red/orange annotation arrows, numbered critique labels, and a compact critique legend.
Critique dimensions: primary action, object hierarchy, data density, decision meaning, duplicate controls, mobile risk, contrast, copy specificity.
Tone: practical product design redline.
Output goal: use image generation as a visual reviewer and feedback surface.
```

If no screenshot exists, ask the image model to create a flawed screen and annotate it. This is useful for teaching and for pressure-testing a concept.

## 6. Before/After Mentor Board

Use when the user wants to learn why a UI direction is weak.

```text
Use case: ui-mockup
Asset type: before/after UX mentor board
Primary request: Create a comparison board with two rows: top row shows weak UI concepts for [product], bottom row shows improved versions of those same concepts after critique.
Composition: [3 columns x 2 rows]. Each column preserves the same concept across weak/improved states.
Weak issues to demonstrate: [feature soup, bad AI panel placement, metrics disconnected from action, weak hierarchy]
Improved moves: [queue-first triage, assistive rail, decision metrics beside workflow, stronger CTA]
Output goal: make critique visible and teach the design move.
```

This works well when Codex needs to explain a design decision to the user before coding.

## 7. Wireframe To Polish

Use when the problem is moving from structure to a credible UI.

```text
Use case: ui-mockup
Asset type: wireframe-to-polish transformation board
Primary request: Show a three-step evolution of [screen]: 1) raw low-fidelity wireframe, 2) structured mid-fidelity layout, 3) polished product UI.
Composition: one horizontal three-panel board with arrows between panels.
Notes to include: object hierarchy, evidence grouping, state visibility, action placement, confidence/risk, and what changed at each step.
Avoid: lorem ipsum, generic dashboard filler, decorative illustration.
Output goal: externalize design progression, not just final pixels.
```

Use this when an implementation task would benefit from a visual bridge between user story and final component structure.

## 8. Convergent Synthesis

Use after selecting promising parts from previous outputs.

```text
Use case: ui-mockup
Asset type: convergent product concept
Primary request: Use these selected ingredients from prior explorations and combine them into one cohesive product concept: [ingredient list]. Design a feature called [name].
Audience: [target user]
Composition: [desktop screen plus mobile companion / one screen plus modal / main workspace plus output artifact]
Layout requirements: [specific regions and relationships]
Interaction details: [what happens when user selects, resolves, approves, shares, exports]
Visual style: [domain-appropriate mood]
Avoid: [failed ideas from earlier rounds]
Output goal: demonstrate convergence into an implementable feature spec and UI.
```

Follow this by writing the build brief. Do not leave the final decision inside the image.

## 9. Practical Handoff From A Selected Mockup

Use after a strong screen exists and the next step is implementation or validation.

```text
Use this selected product screen as reference. Do not make another visual concept. Create a practical handoff artifact for [states | components | design system | responsive behavior | workflow | roles | roadmap | research | accessibility | data model].

Output should be useful to [frontend engineer | product manager | designer | researcher].
Tie every item to visible UI regions, product objects, state, or user actions.
Avoid generic advice.
```

Then choose a specific artifact recipe from [practical-image-loops.md](practical-image-loops.md).

## 10. Brand Guide Image To Asset Pack

Use after the user chooses a generated design or provides an image whose look should guide production assets.

```text
Use case: ui-mockup
Asset type: design-to-assets brief and on-brand asset pack
Primary request: Use the input image as the aesthetic and brand guide. Do not create another UI concept. Extract the brand signals, identify reusable assets, and generate the missing assets needed for [implementation target].
Reference image: [path or selected output]
Preserve: [palette, type mood, density, shape language, line weight, texture/material, icon/illustration style, composition, product tone]
Asset inventory:
- direct extracts: [known visible assets, if any]
- redraw/vector candidates: [assets that need cleanup]
- missing on-brand assets: [icons, empty states, badges, hero art, thumbnails, backgrounds, illustrations, etc.]
- ignore: [fake text, fake logos, decorative artifacts, unrelated motifs]
Production specs: [dimensions, aspect ratios, transparent/full-bleed backgrounds, light/dark variants, states, file formats]
Avoid: copying third-party marks, fake generated copy, generic clip art, decorative filler, and visual motifs not supported by the reference image.
Output goal: create an asset plan, asset prompts, and a lean on-brand asset set that can be implemented in the product.
```

After generation, inspect assets in the actual UI context. Reject assets that only look good in isolation.
