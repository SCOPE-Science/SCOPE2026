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

# Reproduction and limitations

Run `python CHECKER.py` with Python 3 and the standard library. It prints the count of passing assertions, a Monte Carlo illustration, the exact Gaussian finite-grid mean at grid size 65, and the analytic limiting mean. The reproducible run passed 6,155 assertions with empirical mean approximately \(0.008579388\), exact finite-grid mean \(0.008299332\), and limit \(0.007928525\).

The code checks 5,000-plus bridge increment-variance identities with rational arithmetic, the beta-function normalization, the constancy of the expected time-distance row average, the exact finite-grid identity via two separate deterministic computations, complete small-\(n\) permutation averages, and a seeded Gaussian simulation. The analytic manuscript proves the infinite-horizon, full-support, and permutation statements. Finite calculations do not establish those asymptotic claims, nor do they establish publication priority.

The source's independent-increment and finite-variance hypotheses must not be confused with the detrended observations, whose increments are dependent. The exact finite-sample Gaussian expectation is for independent Gaussian input walks and separately normalized endpoint-detrended observations, with all \(n\) time indices included. No claim is made about a dependent-time-valid permutation calibration or about the expectation of normalized squared distance correlation.
