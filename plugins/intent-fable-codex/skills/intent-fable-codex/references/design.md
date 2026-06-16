# Intent Fable Codex Design

## Purpose

Intent Fable Codex is a local prototype for an intent-locked, evidence-gated Codex workflow.

It extracts the best parts of two existing approaches:

- Lightweight routing from `codex-fable-mode`: output lock, depth gate, procedure budget, tool budget, delegation budget, and visible route contract.
- Operational gates from `FableCodex`: goal checkpoints, findings closeout, evidence-backed verification, and final completion discipline.

## Design Principle

Start light. Escalate only when the work earns the process.

Simple answers should stay simple. Small edits should stay small. Large, risky, or ambiguous work should get explicit routing, evidence, and verification gates.

## Routing Stack

```text
User request
  -> intent framing
  -> output lock
  -> depth gate
  -> procedure/tool/delegation budgets
  -> grounding and capability checks
  -> optional goal ledger
  -> optional findings ledger
  -> implementation or answer
  -> final verification
  -> concise report
```

## Output Locks

- `answer`: direct explanation or recommendation.
- `edit`: narrow text, CSS, or code change.
- `implementation`: bounded build/fix/change.
- `review`: findings-first review.
- `audit`: broader risk or quality assessment.
- `design-artifact`: design, architecture, UX, or product artifact.
- `research`: sourced answer.
- `clarification`: ask because acting would be materially risky.
- `validation`: check a claim, behavior, file, link, or artifact.

## Gate Policy

Use no ledger for L0/L1 work unless the user asks.

Use a goal ledger for L2+ work when there are dependent steps or multiple files.

Use findings tracking when missed issues would be costly.

Require final verification when the task changes files, behavior, release state, or claims grounded correctness.

## Non-Goals

This prototype does not:

- copy private prompts
- claim model parity
- add provider routing
- add hooks, MCP servers, or telemetry
- bypass Codex or workspace policy
