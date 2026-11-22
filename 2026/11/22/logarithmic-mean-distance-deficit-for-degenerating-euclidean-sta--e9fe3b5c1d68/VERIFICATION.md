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

The analytic steps are reproduced in RESULT.md: projection-collapse error estimate, exact double straight-side integral, cap error bound, and scale normalization. The independent numerical cross-check is `stadium_check.py` (Python with NumPy and SciPy), run using `python stadium_check.py`. It evaluates all ordered boundary-component pairings; test outputs for four small radii are reported in RESULT.md. Gaussian quadrature does not certify infinitely many radii or the leading constant. No independent mathematical audit has been performed.
