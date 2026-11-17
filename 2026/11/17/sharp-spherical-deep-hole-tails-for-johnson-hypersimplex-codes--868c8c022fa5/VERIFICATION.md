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

The proof uses the coordinate inequalities for the hypersimplex, elementary support-function geometry, the positive-spanning tangent polar, and a closed-form Jacobian evaluation in each sorted-coordinate cone. The probability asymptotic follows from disjoint deep-hole neighborhoods and a uniform first-order change of scale in each bounded tangent polar.

`verify.py` reconstructs all code sites in orthonormal zero-sum coordinates and checks convex-hull facet inradii for \(3\le N\le7\), all admissible ranks. It compares predicted deep-hole support values with finite calculations and verifies that sampled directions satisfy the lower support bound. For \(3\le m\le6\), all rank-relevant tangent polar volumes are computed independently using halfspace intersection plus a convex hull and compared with the closed factorial expression. The checker completed 154 structured checks without assertion failure, using Python 3, NumPy, and SciPy. To reproduce, run `OPENBLAS_NUM_THREADS=1 python verify.py`.

The finite checks do not prove the general infinite-parameter theorem and cannot determine historical originality. No independent audit has been performed.
