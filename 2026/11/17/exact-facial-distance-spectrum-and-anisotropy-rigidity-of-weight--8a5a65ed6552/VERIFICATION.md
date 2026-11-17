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

# Reproducibility and verification

The complete analytical proof is contained in `RESULT.md`. The critical steps are (a) identification of all signed-subset faces, (b) the complement containing the origin for nonfacets, (c) signed coordinate monotonicity plus equality in weighted Cauchy–Schwarz, (d) the complementary opposite-simplex characterization for facets, and (e) a strict comparison of face ranks for the minimizer classification.

The accompanying `check_crosspoly.py` is a standalone executable numerical cross-check. With NumPy and SciPy available, run `python check_crosspoly.py` in the same directory. The program enumerates all signed nonempty proper faces and builds the complementary hull *from the original vertex list*, then uses an independent constrained quadratic minimization over barycentric coordinates of the two hulls. It tests eight weight vectors in dimensions \(2,3,4,5\), totaling 712 face–complement pairs, and checks global minima. The observed numerical maximum error was below \(2\times10^{-13}\); the assertion tolerance in source code is \(3\times10^{-6}\). This is a numerical diagnostic, not a proof for arbitrary reals.

All formulas assume positive semiaxes, a fixed Euclidean metric, and \(d\ge2\). The norm-comparison literature supplies only bounds for arbitrary nonsingular affine maps, so the result does not automatically extend to nonorthogonal cross-polytopes. An independent research audit has not been performed.
