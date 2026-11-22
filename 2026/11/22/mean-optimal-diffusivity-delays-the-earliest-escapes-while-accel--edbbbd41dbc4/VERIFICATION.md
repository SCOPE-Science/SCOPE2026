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

# Verification of the distributional first-passage theorem

Execute `python3 verify.py` from a directory containing the provided `verify.py`. The script requires only Python's standard library. It checks:

- the exact rational Taylor coefficients giving the mean, second moment, variance and squared coefficient of variation;
- the positive rational cubic lower bound for the normalized Bessel series up to \(43/25\), and a numerical bracket for the first positive Bessel zero;
- consistency of the Laplace transform with its hypergeometric series and the homogeneous cosh transform at representative Laplace arguments;
- the exact small-time action and early penalty, the principal-eigenvalue inequality, and a smooth strictly positive regularization via independent shooting integration.

A successful replay gave first zero \(1.866350858874\), normalized optimal first eigenvalue \(2.939005289604\), and homogeneous eigenvalue \(2.467401100272\). At regularization \(\delta=10^{-4}\), the intrinsic action was \(1.087736124\), the mean \(0.444444876\), and the numerical first eigenvalue \(2.938853340\), with unit length and mean diffusivity.

The infinite exponential-sum representation, spectral positivity, early-time limiting asymptotics, and persistence for all sufficiently small positive regularizations are proved analytically in `RESULT.md`; finite experiments do not certify those infinite statements. The interval in which a CDF crossing occurs and the number of its crossings are not determined.
