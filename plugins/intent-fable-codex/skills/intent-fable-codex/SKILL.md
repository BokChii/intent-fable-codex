---
name: intent-fable-codex
description: Use when the user wants Codex to work with an intent-locked, evidence-gated workflow. Apply output locking, smallest sufficient depth, tool and delegation budgets, optional goal ledgers, optional findings tracking, and final verification before claiming completion.
---

# Intent Fable Codex

Intent Fable Codex combines two complementary ideas:

- fable-mode style routing: lock the user's intended output first, then choose the smallest sufficient depth, procedure, tool use, and delegation scope.
- FableCodex style completion discipline: for larger or riskier work, track goals, record evidence, close findings, and verify before saying the work is done.

This skill is procedural guidance. It does not clone a model, bypass policy, add hidden tools, or route to another provider.

## Core Contract

Before acting, classify the request:

1. Intent: what outcome does the user actually want?
2. Output Lock: `answer`, `edit`, `implementation`, `review`, `audit`, `design-artifact`, `research`, `clarification`, or `validation`.
3. Depth: `L0` direct, `L1` small local change, `L2` bounded implementation, `L3` product/design/architecture/debugging, or `L4` risky/hard-to-reverse.
4. Procedure budget: no plan, small inspection, plan-change-verify, audit lanes, or ask-first staging.
5. Tool budget: no tools, minimal reads, bounded edits/checks, runtime/current/visual tools, or explicit approval.
6. Delegation budget: `A0` by default; use read-only specialists only when independent evidence lanes help.
7. Grounding: identify required files, sources, assets, measurements, runtime, or current facts.
8. Completion gate: decide whether plain verification is enough or whether goal/findings ledgers are required.

For L2, L3, and L4 tasks, show a compact route line when useful:

```text
Route: Lock=implementation | Layer=L2 | Procedure=P2 | Tool=T2 | Grounding=repo+tests | Findings=optional
```

The route line is a public work contract, not hidden reasoning.

Keep route fields accurate:

- `Tool=none` only when no tools were used and no tool-backed evidence is needed.
- Use `Tool=T1` when reading skill files, repository files, docs, logs, or other references.
- Use `Tool=T2` when making bounded edits or running narrow checks.
- Use `Tool=T3` when runtime, browser, screenshot, current-source, visual, or asset checks are required.
- Do not say `Procedure=ask-first` unless you actually stop to ask before deciding or implementing.
- If you read this skill or its references before answering, reflect that in `Tool` or `Grounding` instead of pretending the answer was tool-free.

## When To Stay Light

Use the light path for:

- direct explanations
- tiny edits
- narrow validation
- low-risk documentation changes
- user requests that explicitly ask for brevity or no tooling

Light path rules:

- Do not create ledgers for direct answers.
- Do not turn small edits into redesigns.
- Do not run broad checks when a touched-surface check is enough.
- Report only what matters.

## When To Add Gates

Use a goal ledger or equivalent explicit plan when work has two or more dependent steps, multiple files, uncertain root cause, release impact, migration risk, or user-visible behavior changes.

Use findings tracking when:

- a review or audit finds actionable issues
- a subagent or second pass finds defects
- verification failed once and must be tracked to closure
- security, release, migration, or data-loss risk exists

Final completion requires:

- changed or answered scope matches the Output Lock
- explicit constraints were honored
- required evidence was gathered or limitations were reported
- open findings are resolved, rejected with rationale, or explicitly blocked
- verification covers the touched behavior

## Debugging Protocol

For unknown-cause bugs:

1. Reproduce or observe the failure first when possible.
2. Keep at least two plausible causes active; use three for L3/L4 debugging.
3. Gather evidence that distinguishes causes before editing.
4. Fix the causal path, not only the symptom.
5. Verify the original failure mode and the touched surface.

## Reviews

For code review, findings are the product. Lead with bugs, behavioral regressions, missing tests, security issues, and release risk. Use file and line references when available. Do not rewrite the patch unless asked.

## UI And Artifact Work

Do not assume the output is a webpage. Classify the requested artifact first:

- answer, document, code patch, review, app screen, editor, simulator, chart, game, deck, animation, data visualization, or design artifact

Then choose the right substrate:

- DOM, CSS layout, canvas, SVG, WebGL, fixed-frame, asset-grounded media, or hybrid

Renderable or executable artifacts need natural-environment verification, a screenshot/runtime check, a targeted test, or an explicit capability-gap report.

For `design-artifact` outputs, end with the smallest useful next decision set. Name only the choices that would materially change implementation, such as:

- fidelity: conceptual, simplified interactive model, or source-grounded model
- substrate: DOM, canvas, SVG, WebGL, native document, or hybrid
- grounding: provided equations, assets, brand rules, measurements, or explicit simplification
- trigger: whether the next step is implementation, research, visual exploration, or another decision

## Final Response

Keep final reports short:

- what changed or concluded
- what was verified
- what remains risky, blocked, or intentionally out of scope

Do not claim success from intention alone. Completion needs evidence.

## References

- Read `references/design.md` for the combined architecture.
- Read `references/runbook.md` for local installation and validation commands.
