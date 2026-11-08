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

Run `python verify.py` with Python 3 and `mpmath` installed in the same directory. The recorded execution passed 336 exact rational stationary-moment and excess-kurtosis assertions, and 10 high-precision checks of the coefficient series, endpoint integral, exponentially negligible complement and example monotonicity.

This is finite computational evidence supporting, not proving, the universal continuous-parameter theorem. Its proof relies on the stationary Gaussian-convolution representation, independent Poisson backward age, exact Beta-mixture endpoint density, the stationary generator recurrence, an endpoint Laplace asymptotic, and monotone coupling as the contraction parameter changes. Symbolic moment checks do not establish existence, the all-real tail, monotonicity or any originality claim on their own.

Independent audit has not been performed. Publication priority remains subject to additional literature and independent expert assessment; one related stochastic-stiffness paper was available only by abstract.
