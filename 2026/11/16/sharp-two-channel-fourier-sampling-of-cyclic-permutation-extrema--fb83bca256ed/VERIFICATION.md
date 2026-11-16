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

Use Python 3 without third-party packages and run `python3 check_peak_valley.py`. The checker constructs the cyclic peak and valley indicators for every permutation at lengths 5 through 8, computes all covariance entries as exact rational numbers, checks the analytic five-diagonal kernels, verifies their unitary Fourier spectra numerically, checks asserted extremizers through length 600, and samples the asymptotic scaling. The recorded local execution passed 1964 assertions.

The proof of the infinite-family theorem is analytic. The finite loops cannot establish the result for untested lengths, and the approximate asymptotic samples do not prove convergence. The critical local 4- and 5-variable order counts, cyclic disjointness argument, band factorizations, and monotonicity inequalities are stated in RESULT.md for independent reconstruction. No external independent audit has been performed.
