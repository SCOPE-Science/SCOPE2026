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
The self-contained source file `cyclo_weighted_asymmetry_check.py` enumerates exposed vertices by every coordinate order of the Minkowski summands, deduplicates the vertex set, and computes actual minima and maxima of every proper cyclic-tube coordinate sum. It uses exact integers and rational fractions for these comparisons and the claimed asymmetry. An independent linear program with variables \(b_i=(\lambda+1)c_i\) and \(\lambda\) minimizes the containment factor subject to every computed support inequality. The LP is solved with SciPy HiGHS; tolerance is \(10^{-7}\) for the numerical optimum.

Replayed command: `python cyclo_weighted_asymmetry_check.py`.
Observed output: `CYCLIC_WEIGHTED_MINKOWSKI_ASYMMETRY_CHECKS_PASSED profiles= 20 distinct_vertices_total= 5088 tubes_checked= 440`.

The checker covers \(3\le n\le7\) with four positive integer profiles at every dimension. It does not verify arbitrary real coefficients or infinite dimensions by enumeration. Those are covered by the analytical formulas for tube extrema, singleton dominance, and a global reflection-containment lower bound in RESULT.md.

The two primary scholarly papers supplied the simplex-sum representation and standard graph-associahedron facets. Their priority over those premises is preserved. An independent mathematical audit of the new theorem has not been performed.
