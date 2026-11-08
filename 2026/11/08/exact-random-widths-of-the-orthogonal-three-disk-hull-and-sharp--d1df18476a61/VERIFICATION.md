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

The complete theoretical proof is in `RESULT.md`; the optional standalone executable is `verify_width.py` (Python 3 with NumPy and SciPy). A completed execution of that exact script returned:

```
THREE_DIMENSIONAL_CDF_AND_ENDPOINT_CHECKS_PASSED
DIRECT_DISK_SUPPORT_AND_MONTE_CARLO_CHECKS_PASSED
GAUSSIAN_HIGH_DIMENSIONAL_SCALING_CHECKS_PASSED
```

The executable checks the elementary CDF against independently evaluated spherical-band integrals at 81 interior points; exact support maximization numerically approximated by 16,384 points on each of the generating disks for 30 directions; monotonicity, endpoint coefficients, and a 400,000-point seeded Haar-sphere Monte Carlo test; and nonproof numerical illustrations of the limiting law for dimensions 30, 100, and 300.

The numerical disk-support approximation and Monte Carlo are finite. Sharp constants in every dimension, the exact three-dimensional CDF, and the large-dimensional weak convergence are established by the analytic arguments of `RESULT.md`, not extrapolated from finite experiments. Independent mathematical review has not been performed.
