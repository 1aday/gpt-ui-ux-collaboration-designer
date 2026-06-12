# Design Review Inbox Example

This is a small proof case for `gpt-image-ux-partner`.

## Input

```text
Use $gpt-image-ux-partner to improve a product team's UI review workflow.
We want fewer vague AI suggestions and more implementation-ready handoffs.
Use final implementation gate mode.
```

## Before

The starting idea is a generic AI dashboard: assistant panel, unrelated metrics, duplicated actions, and no clear object of work.

![Before: generic AI dashboard](../../assets/examples/design-review-inbox/before-generic-ai-dashboard.svg)

## After

The converged direction is a review queue: each UI issue has a screenshot, risk score, owner, evidence, state, and a clear build-brief output.

![After: review queue to build brief](../../assets/examples/design-review-inbox/after-review-queue.svg)

## What Improved

| Before | After |
| --- | --- |
| Vague AI assistant as the center | A concrete issue queue as the center |
| Metrics are disconnected from action | Evidence sits next to the decision |
| Duplicate CTAs | One primary action: create build brief |
| No handoff artifact | Build brief with components, states, owner, and acceptance checks |
| Advice is hard to implement | Output is ready for a frontend agent |

## Example State

See [`round-notes.example.json`](round-notes.example.json) for the kind of structured state the skill should preserve during a run.

