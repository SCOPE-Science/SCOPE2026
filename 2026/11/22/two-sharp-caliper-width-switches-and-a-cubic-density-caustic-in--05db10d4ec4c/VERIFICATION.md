---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and analytic scope

The width law follows by maximizing the two supports; the stationary equation factors into a linear factor and a quadratic. The minimum-switch proof uses the positive root of a cubic in the square of the stationary slope, then the quadratic relation between that slope and the aspect ratio. Local angle inversion and integration of the scaled derivative, respectively, give the density and width-splitting constants.

The retained supplementary Python diagnostic `parabolic_segment_width_check.py` (Python 3.10+, SymPy, NumPy, SciPy) checks identities and finite examples, with historical output in `CHECKS.txt`. Its check of the maximum-width switch is retained for consistency with the credited diameter result, not as evidence of a distinct contribution. The analytic argument establishes the infinite-parameter claims.
