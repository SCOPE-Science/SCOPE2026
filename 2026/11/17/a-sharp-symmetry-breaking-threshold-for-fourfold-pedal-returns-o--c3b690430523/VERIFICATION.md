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

# Reproduction and boundaries

Run `python3 verify.py` from this package. It is standard-library only. Its deterministic exact-rational tests check the factor identities and derivative reduction. Its independent perpendicular-foot implementation checks both the asserted fourfold similarity and the explicit scale for general points, not merely the proposed maximizers. Checks spanning both sides of the threshold confirm the piecewise expressions.

All-parameter completeness, strict inequalities, equality configurations, and nondegeneracy of the two optimizer points are proved analytically in RESULT.md. Numerical samples alone cannot establish uniqueness or a universal theorem. External independent audit remains unperformed.
