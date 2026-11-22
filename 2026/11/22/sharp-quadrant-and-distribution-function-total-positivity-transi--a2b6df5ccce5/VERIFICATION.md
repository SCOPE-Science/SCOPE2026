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

# Verification and limits

Run `python verify.py` using SymPy. The script symbolically verifies both exact factorizations, the inverse transformation, the critical CDF-TP\(2\) mixed derivative, and rational specializations in all four regimes. Some fixed-point evaluations are diagnostics only; the universal inequalities are analytically proved in RESULT.md using endpoint extrema and a sharp product lower bound. No independent mathematical audit has been performed, and historical uniqueness has not been certified.
