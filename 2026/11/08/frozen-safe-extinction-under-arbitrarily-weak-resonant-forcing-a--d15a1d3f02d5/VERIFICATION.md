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

# Reproducible checks and limits

Run `python verify.py` in an environment with Python 3, NumPy and SciPy. The executed script reports `VERIFY_OK linear_step_checks=79 frozen_profiles=39 forced_crossings=3` and gives the analytical predator kernel bound. It uses 79 matrix-exponential checks, 13 frozen inputs at each of three small amplitudes, and three independently integrated resonantly forced trajectories; numerical grid resolution is finite. The mathematically quantified all-time bounds and extinction mechanism are proved in `RESULT.md`, not by this checker. A forward Filippov continuation at a tangential boundary contact need not be unique; this theorem asserts existence only. There has been no independent scientific audit.
