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
# Reproducibility notes

The theorem follows analytically from the covariance identity, half-line Euler–Maclaurin summation, standard convergence of Gaussian analytic fields, continuity of simple zeros, the Edelman–Kostlan formula and the two scaled saddle estimates. For numerical spot checks run `python CHECK.py` with NumPy and SciPy installed. The checked code evaluates positive gamma-weighted sums and numerical quadratures for five real covariance arguments and three mesh sizes, and tests two asymptotic tail regimes. It returned `PASS 45 finite numerical assertions` for the supplied code. These computations do not establish convergence of the infinite series and are not independent mathematical verification.

The limit concerns the unconditioned family, arbitrary real \(\beta\to\infty\), and compact logarithmic-coordinate windows. The source's conditioned-hole results are different; no inference about conditioning is claimed.
