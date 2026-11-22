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

# Reproducibility and proof evidence

The mathematical argument is presented in `RESULT.md`. `verify.py` is standalone Python, with exact algebra carried out by SymPy and independent numerical covariance computations by NumPy. Install `requirements.txt`, then run `python verify.py` from the directory containing both files.

Successful run checks the Gaussian conditioning formula by direct covariance inversion and an independent Brownian-increment transformation, both first- and second-observation derivative identities, the exact comparison function and its unique algebraic maximum, the coexistence of the two optimal designs at the critical variance, and exact noiseless normalization. It also checks 7,000 reproducibly seeded random competing designs for varied observation times and common-noise variances. The maximum observed covariance formula discrepancy was about \(3.06\times10^{-16}\); no sampled competitor exceeded the analytic optimum.

These calculations are corroborative. The global all-parameter result follows from the strict derivative sign and rational-inequality arguments in `RESULT.md`, not from finite testing. A 2019 closely related Kalman sampling paper was accessible only through its bibliographic abstract, leaving a publication-priority risk; no independent mathematical audit has been performed.
