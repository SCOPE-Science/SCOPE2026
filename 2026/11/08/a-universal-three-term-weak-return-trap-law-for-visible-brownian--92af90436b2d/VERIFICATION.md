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

Execute `python verify_weak_return.py` with Python 3, NumPy and SciPy. The program solves the OU exit mean on the positive interval by an independent collocation boundary-value solver, calculates the positive-side exit probabilities by exact-scale quadrature, integrates the negative-side OU hitting-time derivative, and independently evaluates the continuous-OU comparator.

A run of the included program completed with `PASS numerical checks: 52`. The checks span five independent reset-time laws (exponential clocks of rates 0.25, 1 and 4, and deterministic durations 0.4 and 2), four trap stiffnesses each (0.02, 0.005, 0.001 and 0.0002), strict ordering of the full mean above the OU mean, and controlled relative asymptotic errors. The Poisson cases also check an \(O(\kappa)\)-sized residual against the explicit three-term formula. These tolerances are for numerical corroboration, not certified error bounds or proofs.

The scientific proof uses a globally bounded third derivative of \(\operatorname{erfcx}\) on the nonnegative axis, finite fourth stopped Brownian moments from \(\mathbb E[R^2]<\infty\), optional stopping, and an exact renewal identity. The independent audit status is not_performed.
