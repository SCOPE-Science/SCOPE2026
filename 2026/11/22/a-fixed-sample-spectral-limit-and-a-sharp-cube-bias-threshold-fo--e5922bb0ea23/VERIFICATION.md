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

# Verification record

The claim is mathematically justified by the finite Gram spectral identity, a multivariate Gaussian-coordinate central limit theorem, a bounded triangular-array sign-product central limit theorem, a largest-eigenvalue continuous-mapping argument, quantile continuity, and the all-ones Rayleigh quotient in the strong-signal regime. The exact two-observation specialization additionally reduces to a Beta null law and a binomial alternative law.

Run the standalone `checker.py` with Python, NumPy, and SciPy. In the recorded execution, it passed 751 deterministic assertions, including exact edge-product covariance enumerations for biased signs, the finite-dimensional matrix identities, exact Beta critical quantiles, and binomial powers at multiple dimensions; the optional seeded covariance simulation is supplementary. The checker does not establish infinite-dimensional limit theorems, historical priority, or independent validation.

Scientific scope is limited to fixed sample size \(n\ge2\), ambient dimension \(d\to\infty\), the source's quadratic statistic, independent Haar null directions, and the specified independent-coordinate biased-cube alternatives. Comparison with related literature does not certify novelty; no independent mathematical audit has occurred.
