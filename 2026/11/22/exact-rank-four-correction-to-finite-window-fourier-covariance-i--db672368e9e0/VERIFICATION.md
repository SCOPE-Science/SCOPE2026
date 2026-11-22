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

Run `python3 checker.py` with Python 3; no third-party modules or source datasets are needed. The checker uses exact `fractions.Fraction` arithmetic for a six-point nonresonant two-exponential covariance and for a six-point confluent equal-rate covariance. It reconstructs both covariance matrices, tests each periodization identity entrywise, and uses exact Gaussian elimination to check four-dimensional matrix rank. A separate independent calculation sums the original 240-point stationary Toeplitz covariance in the unitary Fourier basis and reports nonzero complex cross-frequency covariances for three distinct pairs of bins.

The analytic proof in `RESULT.md` covers every positive model rate, every positive sampling interval, every observation-noise variance, and every integer number of observations at least four. Finite checker cases do not establish those universal quantifiers; the elementary matrix identities, generator moment equations, confluent Vandermonde nonvanishing, and positive spectrum arguments do. Gaussianity of actual mRNA counts and correctness of any posterior inference based on the surrogate have not been established.
