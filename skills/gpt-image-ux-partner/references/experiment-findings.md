# Experiment Findings

These findings came from two design labs using image generation for UI/UX brainstorming and practical image-in/image-out iteration.

1. Divergent concept boards work best when the prompt names different interaction models, not just "four ideas."
2. A 2x2 or 3x2 contact sheet is a high-leverage first artifact because it makes weak variety obvious.
3. The model can invent product and growth ideas when asked for user loops, not feature lists.
4. Mobile exploration improves when the prompt explicitly forbids desktop dashboards squeezed into a phone.
5. Visual direction boards are more useful when each tile includes mini UI, swatches, type mood, and density.
6. Critique annotations are useful as a first redline pass, but Codex should verify and rewrite the critique.
7. Before/after boards are excellent for teaching design moves because the contrast is visual and immediate.
8. Wireframe-to-polish boards expose the intermediate structure that is often missing from one-shot UI prompts.
9. Extreme divergence surfaces unusual metaphors, but the next prompt must translate the metaphor into implementable product objects.
10. Convergent synthesis works well when the prompt lists selected ingredients and rejected ideas.
11. Generated UI text is semantically useful but should not be trusted as final copy.
12. Marked-up input images can act as visual selection memory: green keep boxes and red drop crosses can preserve selected ideas across rounds.
13. Region overlays work best when paired with job instructions, not just visual shape instructions.
14. A single polished screen can be expanded into a state coverage board that reveals loading, empty, low-confidence, blocker, response, and completion states.
15. The model can turn a screenshot into an implementation handoff map with component boundaries and likely data objects.
16. Design-system extraction boards can produce token, component, density, and interaction-state drafts from one screen.
17. Responsive adaptation boards are useful when they specify what collapses, moves, or becomes progressive disclosure.
18. Workflow storyboards become more product-useful when each frame names actor, action, state change, and artifact produced.
19. Role-based boards expose permissions and information visibility differences earlier than text discussion often does.
20. Scope slicing boards can turn a visual product idea into Prototype/MVP/V1/V2 phases with explicit exclusions.
21. Usability research boards with UI snippets and behavioral measures are more actionable than generic research checklists.
22. Accessibility audit boards can tie likely issues to visible components, but must be verified with real accessibility testing.
23. Data/event model boards can convert workflow images into draft entities, events, state transitions, and UI-object mappings.

## What Worked Especially Well

- "Do not make visual skins of the same dashboard" reduced cosmetic variation.
- "Each concept must show a different primary object and interaction style" created real divergence.
- "The user loop implied by the UI" pushed feature invention beyond static screens.
- "Callouts that point to actual parts of the UI" produced usable critique boards.
- "Selected ingredients" made convergence more reliable than asking the model to simply "make it better."
- "Weak issue and improved design move" made before/after boards clearer.

## What To Watch

- Contact sheets can make text small. Use them for concept selection, then deepen the chosen idea in a larger single-screen prompt.
- Annotation labels may be visually persuasive but imprecise. Use them to spark critique, not to replace UX judgment.
- The model tends to overuse AI side panels unless told where intelligence should live in the workflow.
- Polished mockups can hide missing empty states, error states, permissions, collaboration details, and data provenance.
- Generated screens often imply fake data models. Extract and normalize those models before implementation.

## Useful Board Types

- **Divergence board:** many concepts, different interaction models.
- **Mobile comparison board:** same job across phone patterns.
- **PLG feature board:** feature ideas with growth loops visible.
- **Visual system tiles:** mood, palette, type, and density.
- **Critique redline:** annotated UX feedback on a screen.
- **Critique-to-redesign:** flawed screen followed by repaired screen.
- **Wireframe-to-polish:** low-fi, mid-fi, and polished progression.
- **Extreme metaphor board:** intentionally broad metaphors for invention.
- **Feature deepening:** one selected idea turned into a real feature.
- **Before/after mentor board:** weak and improved versions side by side.
- **Synthesis board:** selected ingredients combined into one product direction.
- **State coverage board:** same product in loading, empty, ambiguous, blocked, response, and complete states.
- **Implementation handoff map:** screenshot annotated into component/data boundaries.
- **Design-system extraction board:** tokens, components, states, density, and icons extracted from a screen.
- **Responsive adaptation board:** desktop/tablet/mobile behavior and priority order.
- **Workflow storyboard:** actor/action/state/artifact chain across surfaces.
- **Role and permission board:** same workflow across user roles and visibility constraints.
- **Scope slicing board:** Prototype/MVP/V1/V2 with included/excluded capabilities.
- **Usability research board:** UI-linked test scenarios and behavioral measures.
- **Accessibility audit board:** visible UI risks plus concrete implementation fixes.
- **Data/event model board:** entities, events, state transitions, and UI mappings.
