# Local Runbook

## Validate The Plugin

From the workspace root:

```powershell
python plugins\intent-fable-codex\scripts\validate_intent_fable.py
python -m unittest discover -s tests -v
```

## Install From This Workspace Marketplace

This workspace contains a local marketplace at:

```text
.agents/plugins/marketplace.json
```

To make Codex aware of this workspace marketplace, run:

```powershell
codex.cmd plugin marketplace add .
codex.cmd plugin add intent-fable-codex@intent-fable-codex
```

Restart Codex or open a new thread after installing.

## Smoke Prompt

```text
@intent-fable-codex
Review this small change. Lock the output first, avoid over-scoping, and verify only the touched surface.
```

## Expected Behavior

The skill should:

- classify the output lock
- avoid unnecessary process for small tasks
- expose a compact route for L2+ work
- require evidence before claiming completion
- use findings tracking only when it adds value
