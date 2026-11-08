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

# Verification of the price-ordered pinning theorem

Run `python3 verify_star.py` with Python 3 and the standard library. The executable reconstructs the scalar hub/leaf dual allocation; separately obtains the smallest pinned-star eigenvalue using its secular equation; checks selected rational two-price identities with exact fractions; checks random heterogeneous gain assignments and budgets against the claimed optimum; and checks monotonic activation and affine behavior for randomly chosen positive prices.

The packaged script reports 549 rational cases, 400 heterogeneous scalar/secular checks, 6,000 feasible competitor comparisons and 7,600 activation tests, totaling **14,549 supplemental checks passed**.

The script evaluates finite cases only; it does not prove the all-parameter theorem. The analytic proof is given in `RESULT.md`, via a positive leaf-block Schur complement, convex duality, the irreducible symmetric Z-matrix ground-state property and a convex projected epigraph. All costs, eigenvalues and normalization assumptions used in the script agree with the statement in that file. The literature comparison is a self-review and not an independent originality certificate.
