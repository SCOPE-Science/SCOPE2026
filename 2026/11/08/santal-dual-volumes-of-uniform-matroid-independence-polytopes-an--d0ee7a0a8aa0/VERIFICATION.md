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
# Verification

Run `python3 verify.py` with a standard Python 3 interpreter. The code uses no third-party imports. It compares the closed rational polar-volume expression to a separately evaluated signed-facet determinant construction for all \(n\in\{2,\dots,7\}\) and \(1\le k<n\), with three distinct rational interior translations for each rank. It also checks exact equivalence of the derivative of the one-corner rational function and its claimed polynomial equation for \(3\le n\le15\), at four rational test values, plus endpoint signs. The result was `EXACT_CHECKS_OK 141`. A non-package exploratory check independently used convex hulls for dimensions two through six; all agreed with the formula.

The determinant checks are finite corroboration, not a proof for all parameters. The proof in RESULT.md supplies unrestricted formulas, uniqueness and asymptotics. Verification does not establish historical priority, nor does it constitute an independent mathematical audit.
