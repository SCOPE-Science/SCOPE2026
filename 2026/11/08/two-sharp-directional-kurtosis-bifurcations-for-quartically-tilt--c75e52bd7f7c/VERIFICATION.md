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

# Reproducibility checks

Run `python check_quartic_zonal.py` with Python 3 and SymPy. The script computes exact spherical even-monomial expectations independently and checks the proposed closed formula at rational parameters. It also checks all three structural symbolic identities and the contrasting quadratic-tilt strict-monotonicity identity as exact rational-function identities, and repeats a finite grid of sharpness diagnostics (not used as a proof). Actual successful execution recorded:

```
SYMBOLIC_DERIVATIVE_AND_ENDPOINT_DIFFERENCE_IDENTITIES_OK
DIRECT_EXACT_INDEPENDENT_SPHERICAL_MONOMIAL_CHECKS_OK 352
EXACT_FULL_CLASSIFICATION_GRID_DIAGNOSTICS_OK 20412
EXACT_INTERIOR_STABILITY_IDENTITY_OK
ALL_CHECKS_PASSED
```

Proof beyond the finite grid is self-contained in RESULT.md. The verification does not certify all numerical data by exhaustive finite search, any arbitrary-weight extension, or independent mathematical audit.
