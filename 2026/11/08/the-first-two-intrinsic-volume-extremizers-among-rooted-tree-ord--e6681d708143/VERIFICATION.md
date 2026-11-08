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

# Verification and reproducibility

The full proof in `RESULT.md` supplies the infinite argument: vertex-subtree hook counts, the complete facet system with induced Euclidean measure, strict monotonicity of intrinsic volumes under proper inclusion, and the two order-extension constructions. The checks below do not independently certify that proof.

Run `python checker.py` in an environment with Python 3, NetworkX, NumPy, and SciPy. The checker computes facet-area coefficients in \(\mathbb Q+\sqrt2\mathbb Q\) using exact fractions. It separately enumerates upper-ideal incidence vertices and computes Euclidean boundary area from `scipy.spatial.ConvexHull` for small dimensions; this is independent of the hook formula at the area-computation stage. It examines every unrooted tree (up to isomorphism) with every root for \(4\le n\le10\), checking the first/second surface-area levels and the shape profiles. The executed command was `python checker.py` and printed exactly:

`ROOTED_TREE_ORDER_POLYTOPE_CHECKS_PASSED 1803 59 28`

The 1,803 profiles are not the number of distinct rooted-tree isomorphism classes because symmetric root choices are deliberately retained. The 59 convex-hull area checks use sizes through six. Floating-point hull calculations use a relative tolerance of \(10^{-8}\); exact extremal-level comparisons use integer-rational coefficient pairs. The all-intrinsic-volume claim for arbitrary \(n\) rests on the strict-inclusion proof, not on sample enumeration.

No independent mathematical audit has been performed. The source comparison does not prove historical uniqueness. See `REVIEW.md` and `AUDIT.json` for review reasoning and residual risks.
