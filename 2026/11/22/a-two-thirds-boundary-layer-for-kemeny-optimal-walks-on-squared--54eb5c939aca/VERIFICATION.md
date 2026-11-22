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

# Reproducible finite diagnostics

Run `python3 verify.py` with Python 3.9+ and the standard library only. The included program checks the same closed-form resolvent against a direct Fourier sum, the finite-size stationarity equation and derivative sign, perturbations near each computed optimum, an independently assembled transition Laplacian and its Gaussian-elimination inverse on small instances, and scaling constants on larger instances.

The numerical tests produce `PASS 986 finite diagnostics`. Their sample range is finite (typically \(5\le n\le100\) plus six larger sizes) and cannot prove the global uniqueness or large-size asymptotic theorem; those follow from the analytic arguments in `RESULT.md`. The checks use ordinary floating-point arithmetic and tolerances, not exact rational certificates or external validation.
