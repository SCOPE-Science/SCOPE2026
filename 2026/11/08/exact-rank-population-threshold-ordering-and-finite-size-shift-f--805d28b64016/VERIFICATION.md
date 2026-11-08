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

From this directory execute `python verify.py` with Python 3, NumPy, SciPy and mpmath. The script independently checks the time-convolution formula for the single-particle response, high-precision root and shift, beta-quadrature signs and interpolated finite-population thresholds. The validated output prints `PASS`. The numerical examples do not verify every population or every resetting parameter; the all-population sign staircase and asymptotic error estimate are analytic deductions documented in RESULT.md.

All quantities are dimensionless after time rescaling by \(d^2/D\); the mean derivative restores physical units by \(d^4/D^2\). Only local response at zero resetting is proved. Independent audit: not performed.
