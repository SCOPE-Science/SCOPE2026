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

The proof in RESULT.md specifies the hybrid first-hit conventions, exact section map, unique fixed point, local transverse domain, multiplier, cubic flip coefficient and summation argument for the infinite-time relaxation limit. Run `python checker.py` from the extracted package; SymPy and mpmath are required. The script checks exact section and derivative formulas and supplementary finite numerical orbits.

The critical limit and local uniqueness do not follow from numerical tests; they follow from the analytic return and its Taylor expansion. The source comparisons are evidence-limited; historical priority and independent validation have not been established.
