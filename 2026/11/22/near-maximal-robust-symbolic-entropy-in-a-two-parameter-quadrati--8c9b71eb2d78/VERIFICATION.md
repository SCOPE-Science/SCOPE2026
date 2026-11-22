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

# Reproducibility and scope

The formula \(G_{0,4}^{2m}=(L^m,L^m)\) follows from two-step substitution. The derivative bound \(2^m\sqrt{15}/8\) is analytic, not a finite sampling estimate. The inequality \(k_m=\kappa2^m+O(1)\) follows from counting a contiguous interval of integers with at most two endpoint corrections. The limiting sharp entropy benchmark uses the full tent conjugacy and the fact that real logistic orbits outside the unit interval escape, so all compact invariant systems at the limit are contained in the unit square. The inverse sheets have compact images strictly interior to \(J^2\); their nonzero determinants, contraction bounds, and disjointness persist by the uniform inverse function theorem and finite-sheet compactness. No explicit numerical perturbation radius is inferred from test data.

Run `python3 check_horseshoe.py` using the Python standard library. It checks the transformed two-step map, exact sixth-iterate lap indices and endpoint algebra, the lower derivative bound, and finite branch-count examples through the tenth iterate. It does not establish infinite-dimensional or all-parameter conclusions. Reconstructing the proof requires no computationally expensive exhaustive enumeration.

The result proves an expanding one-sided shift on a compact invariant repeller, not a two-sided horseshoe, a positive-area chaotic attractor, an entropy identity on the unbounded entire plane, or a uniform common open neighborhood across all branch depths.
