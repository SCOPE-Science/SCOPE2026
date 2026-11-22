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

The exact killed OU kernel is derived by odd reflection of the unconstrained Gaussian transition density. Integrating it over the half-line and over the exceedance region yields an independent closed-form cross-check for the conditional probability. The late-time coefficients follow from convergent Taylor series in the squared exponential age variable; the sign argument is analytic, not based on finite sampling.

Run `python checker.py` with Python 3, `sympy`, and `mpmath` available. The checker reconstructs the \(e^{-2\kappa t}\) and \(e^{-4\kappa t}\) coefficients symbolically, tests the critical coefficient, directly integrates the absorbing kernel numerically, and samples both asymptotic boundaries and eventually monotone regimes. The local replay passed 56 assertions. No separate external validation or publication-priority certification has been performed.
