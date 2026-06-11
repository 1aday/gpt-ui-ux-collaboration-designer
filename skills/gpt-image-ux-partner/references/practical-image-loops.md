# Practical Image Loops

Use these workflows after a promising concept exists. The goal is to turn images into useful product and engineering artifacts, not to test whether the image model can follow arbitrary tricks.

## Input Image Principles

- Use visual markup only when it encodes a real product decision: keep, drop, preserve, replace, rethink, or prioritize.
- Put labels outside important UI when possible. Messy overlays can still work conceptually, but clean labels produce cleaner follow-up images.
- Make region instructions job-based, not only shape-based: "replace with team state rail that shows blockers, owners, and next actions" is better than "replace bottom bar."
- Feed the best generated output back as the next reference. Treat each image as design memory.
- Ask for artifacts a designer, PM, or frontend agent can use: states, components, breakpoints, roles, access, test plans, data model, events, accessibility risks.

## Design-To-Assets Loop

Use after ideation has produced a design the user likes, or when the user provides a reference image whose aesthetic should guide production assets. The goal is to preserve the chosen visual system while producing real implementation inputs.

### Source Rules

- **Direct extract:** use only for assets that are clear, high enough resolution, and owned or safe to reuse: logo marks supplied by the user, product illustrations, textures, backgrounds, icon shapes, avatar treatments, or UI ornaments that can survive cropping.
- **Redraw/vectorize:** use when the source asset is valuable but the crop would be blurry, partially occluded, text-heavy, or too embedded in the UI.
- **Generate on-brand:** use for missing assets that should match the reference image but do not exist in it: icon families, empty states, hero art, onboarding visuals, state badges, card thumbnails, illustrations, or responsive variants.
- **Ignore:** drop decorative shapes, fake generated copy, impossible UI details, and artifacts that only worked in the mockup.

### Step 1: Make A Brand Capsule

Inspect the selected image and write a compact capsule before generating anything:

```text
Reference image: [path]
Why it was chosen: [layout, mood, brand, product fit]
Preserve: [palette, contrast, type mood, density, corner radius, shadow/material, line weight, icon style, illustration style, texture, composition, product tone]
Avoid copying: [fake copy, fake logos, accidental motifs, third-party marks, unrealistic details]
Implementation target: [web app, mobile app, landing page, design system, feature]
```

### Step 2: Create An Asset Inventory

Use the image as reference and ask for a practical inventory before creating assets:

```text
Use the input image as the aesthetic and brand guide. Create an implementation asset inventory, not another UI concept.

Group assets into:
1) Direct extracts from the image
2) Redraw/vector candidates
3) Missing on-brand assets to generate
4) Assets to ignore

For each asset include:
- intended component or screen
- source region or prompt basis
- target dimensions/aspect ratio
- background requirement
- variants or states
- file format
- verification risk
```

### Step 3: Isolate Reusable Assets

For direct extracts, keep the instruction narrow and production-oriented:

```text
Use the input image as the source. Isolate only [asset name/region] as a clean production asset.

Requirements:
- transparent background unless the asset is explicitly a full-bleed background
- preserve the reference style, edges, color, texture, and lighting
- remove surrounding UI, labels, fake text, and unrelated elements
- output as a standalone asset suitable for [component/use]
- target shape: [square | horizontal | vertical | full-bleed]
```

After extraction, inspect the file in context. Check edges, alpha, resolution, color fit, and whether the crop still reads outside the original mockup.

### Step 4: Generate Missing On-Brand Assets

Use the chosen image as a brand guide, but prompt the new asset's job directly:

```text
Use the input image as the aesthetic and brand guide. Generate [count] new [asset type] for [product/use].

Preserve these brand signals from the reference:
- palette: [notes]
- shape language: [notes]
- material/texture: [notes]
- line/icon/illustration style: [notes]
- density and tone: [notes]

Each asset should:
- support [specific UI state/job]
- fit [component/screen]
- use [transparent background/full-bleed background]
- be [dimensions/aspect ratio]
- share a consistent family style

Avoid: fake UI text, fake logos, unrelated motifs, generic SaaS clip art, decorative filler, and visual details not present in the reference system.
```

Generate assets as sets when family consistency matters. Examples: eight tool icons, six empty states, four state badges, three onboarding illustrations, three responsive hero crops, light/dark variants.

### Step 5: Package The Handoff

Before implementation, write a small manifest:

```text
Asset manifest:
- filename
- source: extracted from [image/region] or generated from [prompt/reference]
- intended component/use
- dimensions/aspect ratio
- variants/states
- accessibility or contrast notes
- verification status
```

Keep the manifest tied to product surfaces. If an asset has no component, state, or user-facing job, do not carry it into implementation.

## 1. Visual Selection Memory

Use when a board has several promising and weak directions.

Create or edit an input image with green boxes around selected ingredients and red crosses over rejected ideas. Then prompt:

```text
Use the visible annotated input image as the design reference. Follow the green KEEP boxes and red DROP crosses as visual instructions.

Create one cohesive, implementable product concept that combines the kept ideas: [ingredient list]. Do not use the rejected ideas: [reject list].

Preserve the structural ideas from the green areas but redesign them into a polished professional product interface. Make it utilitarian, not metaphorical.
```

Discovery: the model can use marked-up images as selection memory. It usually follows the conceptual keep/drop instruction even when the overlay is visually imperfect.

## 2. Region Preserve / Replace Overlay

Use when a generated screen is close, but some regions are wrong.

Mark large regions as:

- PRESERVE: [job]
- RETHINK: [job]
- REPLACE: [new job]

Prompt:

```text
Use the visible annotated screen as an edit/reference target. Follow the overlay instructions literally:
- Preserve [region] because [job].
- Rethink [region] because [problem].
- Replace [region] with [new region] that supports [job].

Create a redesigned product screen. Keep the product domain and workflow. Avoid decorative feature strips or marketing treatment.
```

Discovery: large region overlays work best when the prompt names the new region's job and content, not merely its visual position.

## 3. State Coverage Board

Use before implementation to expose hidden states.

```text
Use this product screen as the reference. Create a practical UX state-coverage board, not a decorative concept board.

Output: one 3x2 board of realistic product screens for the same feature. Each panel should preserve the core product structure but show a different state:
1) loading/ingestion
2) empty/no result
3) low-confidence/needs review
4) blocker/unresolved owner state
5) external response received
6) ready/complete

Each panel should have a short label, primary user action, and state-specific UI. Make it useful for a frontend implementation plan.
```

Discovery: state boards surface loading, empty, ambiguous, collaborative, and completion behavior that a polished single mockup hides.

## 4. Implementation Handoff Map

Use when a frontend agent needs component boundaries.

```text
Use this product screen as the product reference. Create a practical implementation handoff annotation.

Output: one annotated screenshot/board. Overlay numbered callouts and a right-side legend that maps UI regions to implementation concepts.

For each legend item, include:
- component name
- likely data object
- relevant state
- dependencies or events
```

Discovery: a screenshot can become a component/data dependency map. Treat it as a draft architecture sketch, then verify in code.

## 5. Design System Extraction

Use when the visual direction is good and needs to become tokens/components.

```text
Use this product screen as reference. Create a practical design-system extraction board.

Include color tokens, typography roles, spacing/density rules, component specimens, interaction states, icon set, and data-object chips.

Make this useful to a frontend agent implementing CSS/tokens/components. Do not invent a marketing brand guide; extract from the product UI.
```

Discovery: the model can infer a usable component inventory and interaction-state matrix from one screen.

## 6. Responsive Adaptation Board

Use when the screen must survive multiple breakpoints.

```text
Use this desktop screen as the source design. Create a responsive adaptation board with Desktop, Tablet, and Mobile mockups.

Show how the same workflow adapts, not just scales down:
- desktop: multi-column workbench
- tablet: list-detail with collapsible panels and persistent action bar
- mobile: focused task flow with progressive disclosure

Include annotations for what moved, collapsed, or became progressive disclosure.
```

Discovery: the model can produce breakpoint behavior and priority order, not just mobile screenshots.

## 7. Workflow Storyboard

Use when the product loop crosses actors, devices, or async state.

```text
Use this screen as the source product. Create a workflow storyboard with [N] frames.

For each frame include:
- UI surface
- actor
- action
- state change
- artifact produced
```

Discovery: adding "artifact produced" forces the storyboard to reveal useful object/event flow.

## 8. Role And Permission Board

Use when different users need different surfaces.

```text
Create a role-based UX board for the same workflow.

Show [roles]. For each role, show different priorities, hidden/shown information, primary action, and permission/data visibility note.
Avoid making visual skins of the same screen.
```

Discovery: role boards uncover access-control and information-visibility requirements early.

## 9. Scope Slicing Board

Use when deciding what to build first.

```text
Create a product-scope slicing board with columns: Prototype, MVP, V1, V2.

Each column should show:
- small UI mockup
- included capabilities
- deliberately excluded capabilities
- validation question
```

Discovery: image models can turn a concept into product phases with exclusions, which helps prevent overbuilding.

## 10. Usability Research Plan Board

Use when a product idea needs validation before buildout.

```text
Create a usability research plan board for validating the MVP.

For each scenario show:
- UI moment
- task prompt
- what to observe
- success criteria
- likely failure signal
- design change if it fails

Include behavioral measures such as time-to-first-action, confidence explanation, source trust, permission confusion, and recovery from low confidence.
```

Discovery: pairing UI snippets with behavioral measures produces much more useful research plans than generic interview checklists.

## 11. Accessibility And Usability Audit

Use when a screen looks polished but may fail in use.

```text
Create an accessibility and usability risk audit board. Keep the original UI recognizable, but overlay callouts where accessibility or usability could fail.

Tie each issue to visible UI regions and components. Include concrete design fixes and implementation hints for focus order, color-only status, contrast, click targets, screen reader labels, confirmation dialogs, mobile touch targets, and cognitive load.
```

Discovery: the model can generate screen-specific accessibility prompts and implementation reminders. Always verify with actual accessibility checks.

## 12. Data And Event Model Board

Use when visual workflow needs to become product architecture.

```text
Use this workflow storyboard as context. Create a product data-model and event-model board.

Include:
- entity relationship sketch
- event timeline
- UI snippets showing where objects appear
- compact schema cards
- state transitions

Tie the data model to the visible UI and workflow.
```

Discovery: visual workflows can be converted into draft entities, state machines, and event names. The result is not final schema design, but it is an excellent first architecture artifact.
