# Iteration Methods

Image-model UX work is strongest when Codex runs a loop: prompt, inspect, critique, reprompt, extract. Do not stop after the first attractive image.

## Default Six-Round Diverge Then Converge Loop

Use this as the default when the user asks for UI/UX brainstorming and has not requested a shorter path.

### Before Round 1

Ask the user for any missing or unclear framing details from the core frame: scope, audience, user job, primary object, decision/action, device or viewport, business goal, constraints, and avoid-list. Do not invent these silently when they materially affect the design direction.

Set scope explicitly before prompting:

- **Whole site/app:** explore product structure, navigation, key screens, first-screen experience, primary entities, and the core loop.
- **Multi-screen product concept:** explore the main workflow across screens, handoffs, state changes, and generated artifacts.
- **Specific feature:** explore the feature surface, controls, states, evidence, entry point, exit point, and fit with the larger product.
- **Narrow design problem:** explore competing ways to solve one friction point, hierarchy issue, action flow, or responsive constraint.

### Divergent Rounds 1-3

1. Generate a broad concept board, screen set, or focused comparison board that matches the scope.
2. Name the interaction model in each tile.
3. Reject cosmetic variants.
4. Treat each round as both inspiration and failure scouting.
5. After each round, write round notes before generating again.
6. Use the notes to sharpen the next divergent prompt, including a stronger avoid-list based on what failed.

Round notes format:

```text
Round [1/2/3] notes
Liked ideas:
Useful design patterns:
Palette/type signals:
Layout/hierarchy moves:
Product loop or interaction model:
Failure signals:
What felt generic/off-brand:
What looked unbuildable or unrealistic:
What confused the user job or action:
Realism risks or off-brief generated details:
Keep for synthesis:
Drop / avoid because:
Prompt changes for next round:
```

Collect ideas, design patterns, color palette signals, typography mood, layout moves, interaction models, and product loops that are worth carrying forward. Also use the early rounds to discover the bad shape of the problem: unrealistic content, fake features, generated text, irrelevant domain details, over-polished decoration, weak hierarchy, generic SaaS tropes, off-brand visual moves, or anything that would steer implementation in the wrong direction. Convert those findings into the next prompt's constraints and avoid-list.

### Synthesis After Round 3

Review all divergent notes and produce one cohesive direction before convergent prompting:

- selected scope and what is deliberately out of scope
- selected concept and why it won
- target audience and user job
- primary object and interaction model
- core product loop
- main layout and responsive behavior
- visual language, palette, type mood, and density
- features or generated details to reject
- anti-patterns discovered during divergent rounds and why they are rejected
- states, components, and data objects needed for implementation

### Convergent Rounds 4-6

1. Generate one deeper site/app mockup, screen set, feature screen, or focused problem-solution flow from the synthesized direction.
2. Critique it objectively.
3. Preserve only the parts that support the job, product logic, hierarchy, and brand.
4. Tighten the next prompt using the critique.
5. Repeat for three convergent rounds.
6. After round 6, pick the strongest design and proceed with the requested deliverable.

If the user is likely to build it, run one practical handoff loop after selecting the design: state coverage, component map, responsive adaptation, accessibility audit, or data/event model.

## Scope Adaptation Rules

- For a whole site/app, do not over-index on a single pretty hero or dashboard. Extract information architecture, navigation model, first useful screen, core screens, object model, and visual system.
- For a specific feature, do not redesign the entire product unless needed. Extract the feature's entry point, work surface, controls, states, evidence, and completion artifact.
- For a narrow design problem, do not broaden into a new product concept. Compare solution patterns and preserve the exact user friction, constraint, or tradeoff being solved.
- For early product invention, let the images inspire surprising loops and structures, then translate them into realistic product objects and implementation boundaries.
- At every scope, treat image output as directional evidence: useful for layout, hierarchy, palette, interaction model, and big ideas; unreliable for final copy, data, facts, feature feasibility, or domain correctness.

Good convergence prompt:

```text
Keep these ingredients: [A, B, C].
Drop these ideas: [D, E] because [failure reasons].
Avoid these newly discovered anti-patterns: [anti-pattern list].
Resolve these issues from the critique: [issue list].
Design one cohesive [screen/flow] for [audience/job].
Make the UI implementable: name regions, states, actions, and evidence.
```

## Critique Scorecard

Use this after every generated board:

- **User job:** What job does this help the user complete?
- **Primary object:** What object is the user manipulating, reviewing, or deciding on?
- **Primary action:** What is the next meaningful action?
- **Evidence:** What data or context supports the decision?
- **State:** What changes after the action?
- **Rhythm:** Is this for first use, repeated work, triage, comparison, or deep editing?
- **Viewport:** Does the layout fit the intended device?
- **Novelty:** Is this a new product idea or a familiar dashboard in a new skin?
- **Implementation:** What components, data fields, and states would be needed?
- **Risk:** What looks persuasive in the image but might fail in real use?

## Iteration Moves

### Broaden

Use when all outputs look alike.

```text
These are too similar. Generate [6] new concepts that vary by primary object and interaction model. Include one queue, one map/canvas, one dossier, one timeline, one simulator, and one output-artifact workflow. Do not reuse the previous dashboard structure.
```

### Deepen

Use when one concept is promising but shallow.

```text
Take concept [name] and design it as a real feature deep enough to implement. Include the main workspace, key data fields, interaction states, row actions, empty/error/complete states, and one companion view.
```

### Redline

Use when a screen is attractive but suspect.

```text
Create an annotated critique of this screen. Point to specific UI regions. Call out weak hierarchy, missing state, unclear action, over-dense areas, misleading metrics, mobile risk, and copy that sounds vague.
```

### Failure Scout

Use when early rounds look interesting but may contain traps worth learning from.

```text
Use this board as a failure-scouting artifact. For each concept, identify what works and what should not be carried forward.

For each tile, return:
- keepable idea
- failure signal
- why it might fail in real use
- what prompt constraint should prevent this failure next round

Then write a revised avoid-list and a sharper next-round prompt.
```

### Contrast

Use when the user needs to compare approaches.

```text
Show the same product problem solved three ways: [approach A], [approach B], [approach C]. For each, show the tradeoff: what becomes faster, what becomes hidden, and what risk increases.
```

### Constrain

Use when outputs become too decorative.

```text
Redesign this as a working product surface used daily by [audience]. Prioritize scanability, state, evidence, and action. Remove decorative hero treatment, generic illustration, oversized cards, and visual elements that do not support the workflow.
```

### Translate

Use after a selected concept.

```text
From this image, extract a build brief: screen regions, components, data model, controls, states, visual tokens, responsive behavior, and open questions. Separate what is visible in the image from what is an inference.
```

### Operationalize

Use after a screen looks promising but before coding.

```text
Use this selected screen as reference. Create a practical implementation artifact, not a new design direction. Choose one:
- state coverage board
- implementation handoff map
- design-system extraction board
- responsive adaptation board
- accessibility/usability audit
- data/event model board

Tie the artifact to visible UI regions and product objects. Include concrete actions for a frontend/product agent.
```

## Image Input Patterns

When an existing screenshot or generated image is available:

- Use it as an edit target for visual redlines or specific redesigns.
- Ask the model to preserve the parts that already work.
- Identify the image role in the prompt: "edit target", "style reference", "layout reference", or "critique target."
- If using a local image file with built-in image editing, inspect it first so it is visible in context.
- Keep non-destructive copies of selected images when they inform a project or writeup.

## Failure Modes And Fixes

- **Dashboard collapse:** The model returns four dashboards. Fix by requiring different primary objects and interaction models.
- **Pretty but purposeless:** The screen looks polished but has no job. Fix by naming user job, decision, evidence, and post-action state.
- **Literal-copy trap:** The image includes fake features, fake content, impossible data, or unrelated domain details. Fix by extracting only directionality, layout, hierarchy, interaction model, palette/type signals, and big ideas; do not replicate generated specifics without product validation.
- **AI panel bloat:** The AI assistant dominates every screen. Fix by specifying where AI belongs: inline evidence, assistive rail, command palette, critique layer, or generated output.
- **Aesthetic drift:** A round looks impressive but no longer matches the product's intended brand or audience. Fix by naming exact visual invariants and banning the off-brand traits observed in the failed round.
- **Wrong-density drift:** The concept has the right components but the density is wrong for the workflow. Fix by specifying repeated-use density, scanning behavior, and the amount of visible evidence needed before action.
- **Feature soup:** The image invents too many panels, controls, or loops. Fix by naming one primary object, one primary action, and the minimum supporting evidence.
- **Text hallucination:** Labels are garbled or too vague. Fix by treating text as placeholder semantics and rewriting final copy in code.
- **Mobile squeeze:** Desktop tables appear on phone screens. Fix by requiring mobile patterns such as card stack, drawer, timeline, or progressive disclosure.
- **Palette sameness:** Every style tile uses the same hue family. Fix by naming moods and explicit avoid-list.
- **Unbuildable metaphor:** A wild concept has no components. Fix by converging it into rows, panels, fields, actions, and states.
