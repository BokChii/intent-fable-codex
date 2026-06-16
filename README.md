# Intent Fable Codex

Intent Fable Codex is a local Codex plugin prototype for an intent-locked, evidence-gated workflow.

It combines two useful agent habits:

- Start light: lock the user's intended output before planning or using tools.
- Finish honestly: use evidence, findings, and verification before claiming completion.

The result is a Codex skill that helps avoid both over-scoping and under-verifying. Simple answers stay simple. Small edits stay small. Larger implementation, debugging, review, and release work can escalate into goal checkpoints, findings tracking, and final verification.

## Why This Exists

Coding agents often fail in two opposite ways:

- They make the task bigger than the user asked for.
- They report completion without enough evidence.

Intent Fable Codex addresses both by separating task routing from completion gates.

First, it classifies the request:

- output lock: answer, edit, implementation, review, audit, design artifact, research, clarification, or validation
- depth: direct answer through high-risk work
- procedure budget: how much planning and checking is warranted
- tool budget: which tools are necessary and which are just noise
- delegation budget: whether subagents are useful or excessive

Then, only when the work calls for it, it adds stronger gates:

- goal ledger for multi-step work
- findings tracking for review-sensitive work
- final verification before success claims

## Features

- **Output Lock**: chooses the primary deliverable before acting.
- **Depth Gate**: keeps simple work light and gives risky work more structure.
- **Procedure Budget**: prevents tiny tasks from becoming redesigns.
- **Tool Budget**: uses tools for evidence, changes, and verification, not confidence theater.
- **Delegation Budget**: keeps subagents optional, narrow, and evidence-focused.
- **Visible Route Contract**: shows a compact public work contract for substantial tasks.
- **Evidence Gates**: requires verification for behavior changes and grounded claims.
- **Findings Discipline**: tracks review issues until they are resolved, rejected, or blocked.
- **Renderable Artifact Rule**: UI, charts, games, simulations, and executable artifacts need runtime or visual verification when possible.

## Quick Start

Install from this repository as a Codex marketplace:

```powershell
codex.cmd plugin marketplace add BokChii/intent-fable-codex --ref main
codex.cmd plugin add intent-fable-codex@intent-fable-codex
```

For local development from a checkout:

```powershell
codex.cmd plugin marketplace add .
codex.cmd plugin add intent-fable-codex@intent-fable-codex
```

Restart Codex or open a new thread, then invoke:

```text
@intent-fable-codex
Fix this bug with the smallest sufficient workflow. Lock intent first, verify the touched behavior, and report any remaining risk.
```

## Example Route

For substantial work, the skill may expose a compact route:

```text
Route: Lock=implementation | Layer=L2 | Procedure=P2 | Tool=T2 | Grounding=repo+tests | Findings=optional
```

This is not hidden reasoning. It is a user-visible contract for how much process the task deserves.

## When To Use It

Use this skill for:

- implementation work where scope can drift
- debugging with uncertain root cause
- code review where findings should be tracked
- release, migration, or CI work
- UI, chart, game, or simulation work that needs runtime verification
- product, design, or architecture work where output form matters

Skip it for:

- short factual answers
- tiny one-line edits
- tasks where the user explicitly asks for no process

## Validation

Run the local checks:

```powershell
python plugins\intent-fable-codex\scripts\validate_intent_fable.py
python -m unittest discover -s tests -v
```

Validate the Codex plugin manifest:

```powershell
python path\to\plugin-creator\scripts\validate_plugin.py plugins\intent-fable-codex
```

## Repository Layout

```text
.agents/plugins/marketplace.json
plugins/intent-fable-codex/.codex-plugin/plugin.json
plugins/intent-fable-codex/skills/intent-fable-codex/SKILL.md
plugins/intent-fable-codex/skills/intent-fable-codex/references/design.md
plugins/intent-fable-codex/skills/intent-fable-codex/references/runbook.md
plugins/intent-fable-codex/scripts/validate_intent_fable.py
tests/test_intent_fable_codex.py
```

## Boundaries

Intent Fable Codex does not:

- clone or unlock any model
- claim parity with Fable, Claude, OpenAI, or Codex internals
- copy private prompts
- bypass Codex policies, filesystem permissions, or user approval
- add provider routing, network services, telemetry, hooks, or MCP servers

It is a workflow plugin. It improves discipline, not raw model capability.

## Inspiration

This project is inspired by two complementary public Codex plugin experiments:

- `baskduf/FableCodex`, especially evidence checkpoints, goal ledgers, findings gates, and verification discipline.
- `Nam-Cheol/codex-fable-mode`, especially output locking, depth/tool/delegation budgets, and visible route contracts.

This repository is an independent local prototype and does not include code from either project.

## License

MIT. See [LICENSE](LICENSE).
