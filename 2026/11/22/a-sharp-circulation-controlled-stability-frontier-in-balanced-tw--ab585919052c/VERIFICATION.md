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

# Reproducibility and limits

The standalone `check_stage_circulation.py` uses Python 3 with SymPy and NumPy. From the explicit dynamical equations, it constructs the full Jacobian, verifies the orthogonal stage-total/stage-difference block reduction, and symbolically factors the characteristic polynomials of the matched reciprocal and circulating cycles. It checks the exact positive equilibrium, row-balance, matched absolute edge weights, spectral witnesses at \(\Delta=9\), and the critical mixed-mode contact \(g=\sqrt{60}\) with eigenvalues \(\pm6i\).

Additional numerical checks compare the derived all-eigenvalue inequality to direct eigenvalues for general real row-balanced zero-diagonal, potentially nonnormal networks of sizes four, five and seven, and compare the sharp skew-symmetric norm criterion on balanced skew networks. These checks passed on the decoded standalone source. The complete arbitrary-size and all-parameter proof is the determinant and complex-square-root argument in `RESULT.md`, not the finite tests.

The results are local linear-stability statements. At equality the Jacobian has an eigenvalue with zero real part but nonlinear behavior is not established. Independent validation and audit are not performed.
