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

# Reproducibility of the spectral null law

Run `python verify.py` with Python 3 and `mpmath` available (e.g., `python -m pip install mpmath`). The checker uses independent quadrature of the periodic entropy kernel, Fourier-mode numerical integration, beta/digamma identities, a finite Fourier variance partial sum, and an independent Dirichlet-spacing simulation. On the accompanying package, it passed **39 assertions**. It printed the exact-constant numerical evaluation \(0.2801758217380628360735596\ldots\) and first three spectral coefficients \(0.2469859270943188122\ldots\), \(0.0788875730079666566\ldots\), and \(0.03958814958740859499\ldots\).

The analytic proof of convergence of the *original nonlinear score* is in `RESULT.md`, using a normalized exponential-spacing functional CLT, a two-dimensional Riemann-sum limit, and a uniform beta-logarithm endpoint expectation bound. The auxiliary finite numerical tests do not, by themselves, establish an infinite-dimensional limit or historical novelty. The complete original score is distinct from a Gaussian quadratic approximation; the proof controls their difference. No independent mathematical validation has yet been performed.
