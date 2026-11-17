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

The exact domain is the real Type-2 coupled logistic map with first growth coefficient equal to four, \(\mu_1>0\), \(\nu_1>0\), and \(0<\nu_0<\nu_1\), evaluated on its invariant predator-free axis. Initial prey values follow the stationary arcsine law, equivalently an angle uniform on \([0,1)\). The object is the derivative in the one-dimensional normal quotient; it is not an assertion about nonlinear predator trajectories.

The proof is fully contained in RESULT.md: exact Jacobian/quotient derivative, logistic angle-doubling semiconjugacy, log-sine decomposition and zero-mean ergodic theorem, \(L^2\) Fourier coefficient matching, Bernoulli-polynomial evaluation, and finite-n stationary covariance summation. For the two special multiplier zeros, all Bernoulli values and geometric sums are exact rational expressions times \(\pi^2\). A telescope independently identifies the turning-point case.

To repeat computational checks, run `python3 verify.py` with Python 3 (standard library only). The checker verifies 38 exact rational cases, 12 independent finite-Fourier comparisons, 36 exact finite-horizon variance identities, and 24 sample telescoping diagnostics. These checks are not proofs of the infinite-family statements; those depend on the analytic \(L^2\) and ergodic arguments.

Limitations: no external independent audit, no rigorous statement about positive nonlinear predator invasions or global stability, and no statement about exceptional initial angles where a multiplier can vanish. The earlier exact derivative-statistics case is credited to Anteneodo, not claimed as new.
