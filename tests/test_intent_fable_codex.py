from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "intent-fable-codex"


class IntentFableCodexTests(unittest.TestCase):
    def test_manifest_is_installable_shape(self) -> None:
        manifest = json.loads((PLUGIN / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))

        self.assertEqual(manifest["name"], "intent-fable-codex")
        self.assertEqual(manifest["skills"], "./skills/")
        self.assertEqual(manifest["license"], "MIT")
        self.assertIsInstance(manifest["interface"]["defaultPrompt"], list)
        self.assertLessEqual(len(manifest["interface"]["defaultPrompt"]), 3)

    def test_skill_contains_combined_workflow(self) -> None:
        skill = (
            PLUGIN / "skills" / "intent-fable-codex" / "SKILL.md"
        ).read_text(encoding="utf-8")

        for expected in [
            "Output Lock",
            "goal ledger",
            "findings",
            "final verification",
            "Tool",
            "Delegation",
            "Route:",
        ]:
            self.assertIn(expected, skill)

    def test_validation_script_passes(self) -> None:
        script = PLUGIN / "scripts" / "validate_intent_fable.py"
        result = subprocess.run(
            [sys.executable, str(script)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("validation passed", result.stdout)


if __name__ == "__main__":
    unittest.main()
