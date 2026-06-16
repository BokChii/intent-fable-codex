#!/usr/bin/env python3
"""Validate the local Intent Fable Codex prototype."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PLUGIN = ROOT / "plugins" / "intent-fable-codex"
MANIFEST = PLUGIN / ".codex-plugin" / "plugin.json"
SKILL = PLUGIN / "skills" / "intent-fable-codex" / "SKILL.md"
DESIGN = PLUGIN / "skills" / "intent-fable-codex" / "references" / "design.md"
RUNBOOK = PLUGIN / "skills" / "intent-fable-codex" / "references" / "runbook.md"
MARKETPLACE = ROOT / ".agents" / "plugins" / "marketplace.json"


def fail(message: str) -> None:
    sys.exit(f"intent-fable-codex: {message}")


def require_file(path: Path) -> str:
    if not path.is_file():
        fail(f"missing file: {path}")
    return path.read_text(encoding="utf-8")


def validate_manifest() -> None:
    data = json.loads(require_file(MANIFEST))
    if data.get("name") != "intent-fable-codex":
        fail("plugin manifest name mismatch")
    if data.get("version") != "0.1.0":
        fail("plugin version should be 0.1.0")
    prompts = data.get("interface", {}).get("defaultPrompt")
    if not isinstance(prompts, list) or not 1 <= len(prompts) <= 3:
        fail("defaultPrompt must be a list of 1 to 3 prompts")
    for prompt in prompts:
        if len(prompt) > 128:
            fail("defaultPrompt entries must stay under 128 chars")


def validate_marketplace() -> None:
    data = json.loads(require_file(MARKETPLACE))
    entries = data.get("plugins", [])
    match = [entry for entry in entries if entry.get("name") == "intent-fable-codex"]
    if len(match) != 1:
        fail("marketplace must contain exactly one intent-fable-codex entry")
    entry = match[0]
    if entry.get("source", {}).get("path") != "./plugins/intent-fable-codex":
        fail("marketplace source path mismatch")
    policy = entry.get("policy", {})
    if policy.get("installation") != "AVAILABLE":
        fail("marketplace installation policy mismatch")
    if policy.get("authentication") != "ON_INSTALL":
        fail("marketplace authentication policy mismatch")


def validate_skill() -> None:
    text = require_file(SKILL)
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    required = [
        "Output Lock",
        "Depth",
        "Procedure",
        "Tool",
        "Delegation",
        "findings",
        "verification",
        "Route:",
    ]
    for needle in required:
        if needle not in text:
            fail(f"SKILL.md missing required concept: {needle}")
    require_file(DESIGN)
    require_file(RUNBOOK)


def main() -> int:
    validate_manifest()
    validate_marketplace()
    validate_skill()
    print("intent-fable-codex: validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
