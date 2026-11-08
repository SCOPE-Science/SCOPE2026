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
# Reproducibility and limits

The complete proof appears in RESULT.md. Its key identities are the CAR Laplacian, the spectral-multiplier formula, the degree-zero Moore–Penrose lower bound, and the closed-range obstruction to Fredholmness. The unit-scalar example witnesses sharpness of the Hausdorff coefficient. The diagonal projection tuple witnesses noncompact full/essential spectra.

`python CHECKER.py` checks finitely many normal diagonal tuples for CAR, nilpotence and sharp degree-zero lifting. Those finite tests cannot prove the full infinite-exterior Fredholm classification; only the analytic proof does that.

Self-review passed for the stated assumptions; no independent audit has been performed.
