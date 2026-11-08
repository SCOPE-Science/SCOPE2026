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

# Reproducibility

The exact Fourier transform follows from a Laplace integral. The squared magnitude is the hyperbolic-secant-square profile, whose periodization has a Poisson Fourier series and a classical Jacobi elliptic form. The elliptic derivative proves global unimodality; the longer-gap and bank-center evaluations provide strict witnesses for every nonoptimal phase. Consequently the results hold for all positive scale spacings, not just sampled ones.

The accompanying `CHECK.py` requires Python 3 and mpmath and executes 486 finite evaluations that check Fourier quadratures, Fourier/elliptic identities, discrete scale-grid sums, phase witnesses and asymptotic examples. Executing `python CHECK.py` produced `CAUSAL_STAGGERED_WAVELET_CHECKS_PASSED 486`. This computation does not prove infinite-parameter statements; the universal proof appears in RESULT.md.

The result covers complete, bi-infinite geometric scale banks with continuous translations. Finite banks, sampled translations, changes of normalization and implementation errors are not included. Independent validation has not been performed.
