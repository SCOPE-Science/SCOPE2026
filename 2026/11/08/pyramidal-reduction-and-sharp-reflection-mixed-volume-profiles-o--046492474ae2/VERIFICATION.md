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

# Reproducible verification

Run `python verify.py` using Python with `scipy` and `numpy` available. The script checks exact rational coefficients of the two-slice polynomial, tests derivative signs and endpoint continuity, and independently compares predicted three-dimensional Minkowski sum volumes with the convex hull of pairwise sums of original vertices. The self-contained script runs without network access.

The proof of the all-dimensional claim is analytic: exact horizontal-section inclusions, exact integration of mixed-volume polynomials, and positivity of the derivative sign factor. The numerical hull checks and finite exact-rational cases do not establish the infinite-dimensional universal claim on their own. The sharp comparison invokes the established Godbersen inequality and equality theorem; neither is independently reproduced here. Historical-priority assessment remains provisional.
