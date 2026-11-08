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

# Reproducible verification of cactus-graph Mahler factors

The package contains `check_cactus_mahler.py`. Run `python check_cactus_mahler.py` with Python, NumPy, and SciPy available. The code uses no external files or network access. It evaluates the alternating-sum central cube density in exact rational arithmetic, checks the first eight reported factor values and additional rational factors through cycle length \(19\), and uses independent Euclidean convex-hull calculations to obtain both the primal and polar volumes.

Expected success marker: `CACTUS_MAHLER_CHECKS_PASSED 12 hull tests, rational cycles 3..19`.

The twelve polytope tests comprise cycles on \(3\) through \(8\) vertices, two trees, a triangle with bridges, two attached triangles, and a triangle with an attached quadrilateral. The polar is constructed from the facet inequalities of the primal hull rather than from the asserted cube-section formula. Numerical relative tolerance is at most \(5\times10^{-7}\), reflecting floating-point convex-hull calculations. The exact rational tests have no such tolerance.

The universal proof rests on four noncomputational steps: free-sum polar/volume product, edge-difference determinant, odd/even facet triangulations, and Laplace/Stirling asymptotics. The checker independently corroborates small instances of the first three; it is not an exhaustive proof or an external certificate. The final mathematical assessment is a self-review only, without independent validation.
