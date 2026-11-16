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

# Verification record

Proof dependencies: (i) unique trace-normalized quadratic for each nondegenerate filled ellipse; (ii) strict sign of the difference of normalized defining quadratics on the symmetric difference; (iii) invariance of domain for the dimension-five parameter manifold; (iv) positive-part convex supporting inequality; (v) coarea differentiation and the no-vanishing-traceless-quadratic lemma on the ellipse boundary; (vi) trigonometric orthogonality determining the unweighted Gram determinant. These steps are explicitly proved in `RESULT.md`.

Numerical confirmation: run `python ellipse_moment_checker.py` with Python, `numpy`, and `scipy`. Three displaced noncircular ellipses were checked; every analytic boundary Gram agrees with finite differences of moment derivatives to better than \(5.1\times10^{-10}\) entrywise in the tested cases. Every smallest Gram eigenvalue was positive, the determinant lower bound held, and convex numerical recovery was within \(2.1\times10^{-7}\) in normalized parameter Euclidean norm. The expected terminal message is `GAUSSIAN_ELLIPSE_FIVE_MOMENT_TOMOGRAPHY_PASS cases=3`.

Limits: finite numerical checks cannot prove the universal theorem. The theorem is analytical and assumes a calibrated Gaussian density, a single nondegenerate ellipse and exact complex data. No independent audit has occurred.
