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

# Verification of the four-cycle consensus theorem

Run `python verify_c4.py` in the same directory with Python 3 and SymPy. It reconstructs the \(2\times2\) covariance-action matrix from all \(16\) Bernoulli edge-activation masks for each spectral projector. The executed test passed the exact matrix identities, the similar symmetric matrix and positive-definite quadratic coefficient determinant, the spectral discriminant, the derivative reduction, the critical-probability factorization, and two exact rate evaluations.

The critical mathematical claims independent of finite computations are: dihedral invariance reduces the repeated covariance dynamics to two modes; Perron–Frobenius gives the asymptotic rate for every nonconstant initial vector when delivery probability is strictly between zero and one; strict Loewner convexity makes the optimizer unique; and sign analysis identifies the exact threshold within the legitimate unsquared branch. Those steps are given in `RESULT.md`. The checker is supplementary algebraic verification, not a statistical or infinite-iteration certificate. Historical priority and independent mathematical audit have not been established.
