# GPT UI/UX Collaboration Designer

This repo packages the Codex skill `gpt-image-ux-partner`.

It turns GPT image generation into a practical UI/UX collaborator: divergent design boards, critique/redlines, failure scouting, convergence rounds, and implementation-ready design or asset briefs.

## Install With Codex

In Codex, point at this repo and say:

```text
Install the skill from https://github.com/1aday/gpt-ui-ux-collaboration-designer/tree/main/skills/gpt-image-ux-partner
```

Codex's built-in `skill-installer` can also install it directly:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-installer/scripts/install-skill-from-github.py" \
  --repo 1aday/gpt-ui-ux-collaboration-designer \
  --path skills/gpt-image-ux-partner
```

Restart Codex after installation so the skill is picked up.

## Local Install

If you cloned the repo:

```bash
git clone https://github.com/1aday/gpt-ui-ux-collaboration-designer.git
cd gpt-ui-ux-collaboration-designer
./scripts/install.sh
```

## Use

After installing, invoke it by name:

```text
Use $gpt-image-ux-partner to explore UI/UX directions for this app before coding.
```

Useful prompts:

```text
Use $gpt-image-ux-partner to run a scope-calibrated UI/UX ideation loop for a mobile feature. Ask me for missing scope, audience, viewport, or constraints before generating.
```

```text
Use $gpt-image-ux-partner to critique this screenshot, identify failure signals, then converge on an implementation-ready redesign brief.
```

```text
Use $gpt-image-ux-partner to turn the selected mockup into an asset plan: direct extracts, redraw candidates, and missing on-brand assets.
```

## What The Skill Does

- Sets scope first: whole app/site, multi-screen product concept, specific feature, or narrow design problem.
- Runs three divergent rounds, using each round for design inspiration and failure scouting.
- Keeps round notes: liked ideas, useful patterns, palette/type signals, layout moves, failure signals, and next prompt changes.
- Synthesizes one cohesive direction before convergence.
- Runs three convergent rounds to refine hierarchy, states, responsiveness, realism, and product logic.
- Treats image output as directional inspiration, not literal implementation truth.
- Converts the selected direction into build briefs, component maps, responsive notes, or asset plans.

## Repository Layout

```text
skills/gpt-image-ux-partner/
  SKILL.md
  agents/openai.yaml
  references/
scripts/install.sh
```

## Validate

From the repo root:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" \
  skills/gpt-image-ux-partner
```

The expected result is:

```text
Skill is valid!
```

