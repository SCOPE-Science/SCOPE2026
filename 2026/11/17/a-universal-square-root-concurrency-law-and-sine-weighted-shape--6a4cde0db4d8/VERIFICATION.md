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

# Reproducible verification

Run `python verify_random_routh_cevians.py` with NumPy and SciPy installed (versions unrestricted). Successful execution ends with `ROUTH_CEVA_SQRT_AND_ANGLES_CHECK_OK`. It checks exact polynomial area against direct line intersections for 120 independently sampled triples; verifies the leading \(3\pi/4\) constant by adaptive two-dimensional quadrature; simulates 1,800,000 triples for each of three thresholds; and checks the conditional auxiliary acute frequency against \(1/\pi\).

Observed threshold, empirical probability, leading prediction, and ratio of empirical to prediction:

| Threshold | Empirical | Leading | Ratio |
| --- | --- | --- | --- |
| 0.01 | 0.220670556 | 0.235619449 | 0.9365549 |
| 0.001 | 0.072931667 | 0.074509412 | 0.9788249 |
| 0.0001 | 0.023564444 | 0.023561945 | 1.0001061 |

This is finite numerical corroboration. The analytic proof uses the integral formula, domination and Jacobians, and does not infer any infinite statement from simulations. No independent audit is reported.
