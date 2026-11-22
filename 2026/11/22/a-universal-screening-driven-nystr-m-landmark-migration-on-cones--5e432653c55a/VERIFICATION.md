---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and limits

`verify_cone.py` is a standalone Python 3 checker depending on SymPy, NumPy and SciPy. Execute `python verify_cone.py` from a directory containing the extracted artifact. It constructs eleven explicit base graphs, including cycle rims, the Petersen graph, the triangular prism, and several complete bipartite graphs; it checks exact matrix and trace formulas for multiple rational positive screening parameters. It also checks the exact four-rim threshold and numerically compares five wheel thresholds with the analytical asymptotic coefficient.

The actual local execution printed: `PASS: 1483 exact symbolic/rational assertions and asymptotic comparisons over 11 test graphs`. The universal theorem depends on the printed mathematical proof, **not** on testing a finite collection of sizes or screening values. No external mathematical verification or publication-priority certification has occurred.
