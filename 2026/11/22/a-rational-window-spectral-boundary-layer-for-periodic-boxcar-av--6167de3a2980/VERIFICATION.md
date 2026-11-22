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

The numerical checker is standalone Python 3 and uses only the standard library. Run `python check.py` beside the other packaged files. It checks Fourier normalization, rational and irrational threshold counts, the small half-window-detuning regime, and the strict resonance dip. The analytic proof does not use floating-point inference. The inverse noise-risk problem, convergence rates for arbitrary irrational windows, and global uniform parameter bounds are not asserted. Independent verification has not been performed.
