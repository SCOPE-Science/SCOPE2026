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

Run `python3 check_biclique_mahler.py` in an environment with Python 3, NumPy and SciPy. The checker performs exact-rational double integration and exact \(h^*\)-formula comparisons over 144 ordered pairs, the equality boundary \(\min(p,q)\le2\), and applicable strict coordinate monotonicity comparisons; it also independently computes intrinsic primal and polar volumes with Euclidean convex hulls in seven small cases, including the nontrivial \(K_{3,3}\) case.

Expected terminal markers: `exact_integral_hstar_and_monotonicity_144_pairs PASSED` and `CONVEX_HULL_CHECKS_PASSED 7`.

The analytic proof in RESULT.md proves the all-dimensional claims. Finite exact arithmetic and floating-point ConvexHull results are cross-checks only, and do not establish historical novelty or independent validation.
