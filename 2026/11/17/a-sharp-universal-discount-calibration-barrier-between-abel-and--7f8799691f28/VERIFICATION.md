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
# Reproducible checks

Execute `python3 check_abel_cesaro.py` in the same directory as this file. The checker uses Python's standard library only. The observed successful test categories are: exact rational coefficient-versus-uniform/geometric total variation on 1,800 finite cases; 225 sign-witness checks of the sharp unilateral-shift evaluation; an independent finite-active-interval critical-point candidate comparison for \(2\le n\le44\); numeric bracketing of the unique limiting stationarity equation; and numerical convergence of finite-horizon discrepancies to the analytic limit.

The unrestricted proof, including uniqueness and localization of minimizers, is in RESULT.md. A finite test is neither an exhaustive check across all dimensions nor proof of a limiting assertion. No external independent audit or mathematical certification has been performed.
