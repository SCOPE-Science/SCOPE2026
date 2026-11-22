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

The analytic proof in `RESULT.md` establishes the exact stationary mode diagram from a positive beta-mixture formula and a scalar hypergeometric differential equation. The unique off-center critical points are found by a one-dimensional hypergeometric root equation, with no finite-grid assumption. The opening-law constant is derived by an integrable rescaling limit and the beta reflection identity.

To repeat the computational diagnostics, install Python 3 with `sympy` and `mpmath`, then execute `python check_modes.py`. The checker was run against the final standalone code file and passed 410 assertions. It covers a symbolic differential-equation identity; 336 exact stationary moment relations; 28 exact resonance-density comparisons; 21 differential-equation numerical residuals; five bracketed critical roots; and four splitting-scale samples, plus two symbolic coefficient identities and 14 root/scale checks. The precise count can be reproduced from the script output; individual examples are supplemental and do not establish the continuum theorem.

The derived theorem does not include translational noise, nonlinear traps, aperiodic run-length laws, unbiased-to-biased extensions, or any finite-time mode diagram. Literature search and independent scientific validation are not mathematical proof of publication priority. No independent audit has been performed.
