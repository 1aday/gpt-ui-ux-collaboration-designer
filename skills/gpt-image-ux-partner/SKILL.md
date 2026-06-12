---
name: gpt-image-ux-partner
description: "Use GPT image generation as a UI/UX brainstorming, critique, convergence, and design-to-assets partner at any product scope: whole site or app mockups, multi-screen product concepts, specific feature UX, product-led growth loops, mobile flows, visual systems, color palettes, typography directions, narrow design-problem solving, screenshot redlines, before/after UX critique, implementation-ready design directions, asset extraction from selected images, and on-brand asset generation using a chosen image as the aesthetic or brand guide. Use when Codex needs divergent and convergent design exploration, creative feature invention, visual feedback on an existing screen, a stronger product/UI concept before coding, or an implementation asset plan after a design is chosen."
---

# GPT Image UX Partner

Use image generation as a design-thinking surface and inspiration channel, not as an automatic source of truth. The model can invent layouts, visualize feature ideas, compare interaction models, annotate problems, and synthesize directions quickly. Codex remains the product critic: inspect outputs, reject weak ideas, extract structure, and translate the selected concept into an implementable spec.

## Operating Stance

- Treat generated images as sketches from a fast visual collaborator.
- Start by asking the user which collaboration cadence they want unless they already specified it: step-by-step feedback, autonomous sprint, or final implementation gate.
- Set the scope first: whole site/app, multi-screen product concept, specific feature, or narrow design problem.
- Ask for interaction models, objects, loops, and constraints before asking for style.
- Prefer contact sheets for divergence and single-screen mockups for convergence.
- Critique every output. Do not accept a pretty screen unless the workflow, hierarchy, and user job hold up.
- Extract directionality, layout, interaction ideas, and visual signals from images; do not literally copy unrealistic generated features, fake content, or off-domain artifacts.
- Keep round notes during ideation: liked ideas, useful design patterns, palette/type signals, layout moves, failure modes, realism risks, and decisions to keep or drop.
- Use early divergent rounds as diagnostic probes. Look for what can go wrong, what feels off-brand, what becomes unbuildable, what confuses the user job, and what the next prompt should avoid.
- Maintain an evolving avoid-list and anti-pattern ledger. After each round, turn observed failures into sharper constraints for the next exploration.
- Preserve prompts and selected image paths when outputs inform later implementation.
- For user-provided screenshots or local images, inspect them first, then use image editing or a generated critique board to annotate issues.
- After a design direction is chosen, treat the best image as design memory: a visual brief for layout, mood, palette, density, typography, shape language, illustration style, and asset tone.
- Separate asset work into three buckets: assets to isolate from the image, assets to redraw or vectorize from the image, and missing assets to generate on-brand from the image as aesthetic reference.
- Do not blindly trace a generated screen into production. Extract the design system and asset intent, then verify actual crops, transparency, dimensions, contrast, and licensing before implementation.

## Workflow

1. **Choose the collaboration cadence.**
   Before framing or generating, ask the user how they want to collaborate unless they already made it clear:

   - **Step-by-step feedback:** pause after each divergent round, synthesis, and convergent round so the user can react, redirect, or choose.
   - **Autonomous sprint:** Codex keeps going, decides between rounds, updates the avoid-list and synthesis itself, and asks only when blocked or when a decision would be risky.
   - **Final implementation gate:** Codex runs the ideation and convergence loop autonomously, then asks once before implementation, asset production, or code changes.

   Treat the answer as the default cadence for the session. In autonomous modes, keep concise notes so the user can audit the decisions later. In final-gate mode, do not implement until the user approves the chosen direction.

2. **Frame the design problem.**
   Capture the scope, audience, job, primary object, decision/action, device or viewport, business goal, constraints, and avoid-list. If any of these aspects are unknown or unclear, ask the user before generating. Keep questions short and only ask for what is needed to avoid designing the wrong product.

3. **Choose the exploration mode.**
   Use the mode that matches the design question:

   - **Divergent concepts:** ask for 4-8 different interaction models, not visual skins.
   - **Whole site/app mockup:** ask for product shape, navigation, key screens, first-screen experience, system objects, and core loop.
   - **Feature invention:** ask for product loops, primary objects, and screens that imply how the feature grows or gets reused.
   - **Specific feature UX:** ask for feature states, controls, evidence, edge cases, and how the feature sits in the existing product.
   - **Narrow design problem:** ask for multiple ways to solve the exact friction, tradeoff, information architecture issue, or action flow.
   - **Mobile constraint solving:** ask for side-by-side mobile patterns and forbid squeezed desktop dashboards.
   - **Visual language:** ask for style tiles with mini UI, palette swatches, type mood, and density notes.
   - **Critique/redline:** ask for annotated callouts on the actual or recreated screen.
   - **Before/after mentorship:** ask for weak concepts and improved versions in the same board.
   - **Wireframe-to-polish:** ask for staged evolution from raw structure to refined UI.
   - **Convergent synthesis:** feed selected ingredients back into one cohesive feature or screen.
   - **Practical handoff:** derive states, components, data objects, responsive behavior, roles, accessibility risks, or test plans from a selected mockup.

4. **Run three divergent rounds as exploration and failure scouting.**
   Use image generation with structured prompts scaled to the scope. For each round, ask for a 2x2, 3x2, or 4x2 board, multi-screen set, or focused comparison board. Force each tile to vary by primary object, interaction style, or problem-solving strategy. Add anti-requirements such as "do not make four skins of the same dashboard." After each round, write notes on the ideas, patterns, palette, typography, layouts, and product loops worth carrying forward, plus what went wrong, what looked generic, what felt off-brand, what would be unbuildable, and what generated details to reject as unrealistic or off-brief. Use those failure notes to sharpen the next prompt.

5. **Inspect as a product designer.**
   Score the output on:

   - Job fit: does it help the intended user make progress?
   - Structural novelty: is it a different interaction model or just a reskin?
   - Primary object clarity: can you name what the user manipulates?
   - Action clarity: is the next move obvious?
   - Information hierarchy: does the screen privilege the right evidence?
   - Viewport realism: would it survive desktop, mobile, or dense repeated use?
   - Implementability: can this become routes, components, data fields, and states?
   - Visual direction: does the mood fit the domain without becoming decoration?
   - Failure signal: what does this reveal that the product should avoid?
   - Prompt learning: what should change in the next prompt based on this result?

6. **Synthesize after divergent round 3.**
   Review all round notes and produce one cohesive direction that is neat, on-brand, and buildable. Name the selected concept, the reasons it won, the interaction model, primary object, visual language, layout system, palette/type direction, core states, and the generated ideas being rejected. Include an explicit "avoid because" list so convergence is guided by both what worked and what failed.

7. **Run three convergent rounds.**
   Refine the synthesized direction through three single-screen or focused-flow generations. Each round should preserve the chosen product logic while improving hierarchy, layout, visual system, states, responsiveness, and realism. Pick one of these moves per iteration:

   - Keep: preserve a promising direction and deepen it.
   - Reject: name why a direction fails and ask for alternatives.
   - Merge: combine selected ingredients from multiple outputs.
   - Tighten: add constraints such as device, data density, accessibility, or state.
   - Redline: ask for annotated critique on the image or a recreated flawed screen.
   - Translate: turn the chosen direction into an implementation brief.

8. **Pick the best design and act on it.**
   After convergent round 3, choose the strongest design objectively, explain why it wins, and do the next requested work from that direction: implementation, final mockup, handoff, or written product spec. Extract a written design brief before coding:

   - chosen concept and why it won
   - audience and job
   - primary object model
   - main screen structure
   - core user loop
   - key components and controls
   - data fields, states, and edge cases
   - visual system notes
   - explicit non-goals and rejected ideas

9. **Convert the chosen design into usable assets when needed.**
   If the next step is implementation, brand exploration, or production design, use the selected image or user-provided image as the aesthetic guide. First write an asset brief before generating or cropping:

   - source image path and why it was chosen
   - brand signals to preserve: palette, type mood, density, radius, shadows, textures, line weight, icon style, illustration style, composition, and product tone
   - asset inventory grouped as direct extracts, redraw/vector candidates, generated-on-brand additions, and unnecessary decorative pieces to ignore
   - required production specs: file type, aspect ratio, target size, transparent background, light/dark variants, states, responsive variants, and accessibility constraints
   - prompts and negative prompts for missing on-brand assets

10. **Isolate what can be reused directly.**
   For assets visible in the chosen image, crop or isolate only if the asset is actually useful in production: logo marks owned by the user, icons, product illustrations, textures, backgrounds, avatars, empty-state art, or hero/media treatments. Prefer clean transparent-background assets when possible. If the source is a generated mockup, treat isolation as a draft and be ready to redraw or recreate the asset cleanly.

11. **Generate the missing on-brand assets.**
   Use the chosen image as the brand and aesthetic reference, then prompt for only the missing pieces. Keep prompts specific about role, dimensions, background, style invariants, and what must not drift. Generate assets as sets when consistency matters: icon family, empty states, avatar set, product illustration set, texture pack, hero image, card thumbnails, state badges, or onboarding visuals.

12. **Package the asset handoff.**
   Before coding, create a small implementation handoff: asset manifest, filenames, intended component/use, dimensions, variants, source prompt/reference image, and any verification notes. Keep the asset set lean; do not generate decorative filler just because the source image looks good.

## Prompt Skeleton

Use only the fields that matter:

```text
Use case: ui-mockup
Asset type: <divergent concept board | mobile flow board | critique redline | visual system tiles | convergent screen | design-to-assets brief | asset isolation sheet | on-brand asset pack>
Scope: <whole site/app | multi-screen product concept | specific feature | narrow design problem>
Primary request: <what the image should help decide>
Audience: <target user>
User job: <task or decision>
Business/product context: <domain and goal>
Brand/aesthetic reference: <selected generated image path or user-provided image path, plus what to preserve>
Composition: <2x2 board, 3 mobile screens, one desktop screen, before/after grid, etc.>
Required variety: <different interaction models, product loops, metaphors, device patterns>
Must include: <primary object, actions, evidence, states, controls>
Asset plan: <direct extracts, redraw candidates, missing on-brand assets, variants>
Failure scouting: <what to test for, what can go wrong, anti-patterns to avoid next>
Constraints: <viewport, density, accessibility, brand/system constraints>
Avoid: <dashboard skins, generic AI copilot, marketing hero, decorative gradients, vague labels>
Output goal: <what Codex should learn from the image>
```

## Strong Prompt Moves

- Say "different interaction models" instead of "different designs."
- Name concept archetypes when you need real variety: map, queue, dossier, workbench, timeline, canvas, wizard, triage, simulator, memo, scorecard.
- Ask for "the user loop implied by the UI" when exploring product ideas.
- Ask for "selected ingredients" when converging from multiple outputs.
- Ask "what should we avoid after seeing this?" after each divergent board.
- Ask for "weak version plus improved version" when the user needs critique or teaching.
- Ask for "callouts that point to actual parts of the UI" when generating design feedback.
- For mobile, explicitly forbid "desktop dashboard squeezed into mobile."
- For visual systems, ask for swatches, type mood, density, and one-word personality labels.
- For post-ideation asset work, say "use the input image as the aesthetic and brand guide" and name the invariants to preserve.
- Ask for an asset inventory before generating assets: direct extracts, redraw candidates, missing on-brand assets, variants, and assets to ignore.
- For generated asset packs, specify count, use case, dimensions, background, export style, state variants, and shared family traits.
- For brand-matched additions, forbid copying fake text, fake logos, or ornamental details that do not support the product.
- Convert observed failures into the next prompt's avoid-list instead of leaving them as passive critique notes.

## Known Limits

- Generated text is useful as semantic placeholder copy, not final copy.
- Beautiful UI screenshots can hide weak product logic. Always extract the user loop.
- Image models often collapse divergent prompts into dashboard variants unless told to vary the primary object and interaction model.
- Redline annotations are good for surfacing issues, but Codex should still verify the critique.
- Do not trace the image literally when implementing. Use it as a source of layout, object, hierarchy, and workflow ideas.
- Asset isolation from a mockup can be messy. Verify edges, resolution, transparency, and visual fit in the real UI.
- A brand guide image can overfit the next generation. Preserve explicit invariants and reject accidental artifacts, fake copy, or unrelated motifs.
- Do not reuse third-party logos, trademarked characters, or owned brand assets unless the user owns or has permission to use them.

## References

- For reusable prompt recipes, read [references/prompt-patterns.md](references/prompt-patterns.md).
- For iteration methods and critique heuristics, read [references/iteration-methods.md](references/iteration-methods.md).
- For image-input loops that create implementation-useful artifacts, including selected-image asset extraction and on-brand asset packs, read [references/practical-image-loops.md](references/practical-image-loops.md).
- For experiment-derived findings from the original design lab, read [references/experiment-findings.md](references/experiment-findings.md).
