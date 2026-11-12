"""The README promises a zero-dependency crawler, so enforce it in CI."""

from __future__ import annotations

import ast
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]


class NoThirdPartyImportsTest(unittest.TestCase):
    def test_sources_only_import_stdlib_and_local_modules(self):
        stdlib = set(sys.stdlib_module_names) | {"src", "classify", "fetcher", "main"}
        offenders: list[tuple[str, str]] = []

        for path in sorted((ROOT / "src").rglob("*.py")):
            tree = ast.parse(path.read_text(encoding="utf-8"))
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        root = alias.name.split(".")[0]
                        if root not in stdlib and root != "src":
                            offenders.append((path.name, alias.name))
                elif (
                    isinstance(node, ast.ImportFrom) and node.level == 0 and node.module
                ):
                    root = node.module.split(".")[0]
                    if root not in stdlib and root != "src":
                        offenders.append((path.name, node.module))

        self.assertEqual(offenders, [], f"third-party imports found: {offenders}")


if __name__ == "__main__":
    unittest.main()
