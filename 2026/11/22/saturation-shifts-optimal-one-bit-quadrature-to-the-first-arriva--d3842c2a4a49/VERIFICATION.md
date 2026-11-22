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

Use Python 3.10 or later with its standard library; run `python verify.py` in this directory. This executes 7,219 checks: direct objective-grid comparisons for 18 rates/population sizes, unique positive-root and asymptotic spot checks, monotonicity comparisons, and independently simulated conditional and unconditioned event-time samples with a fixed seed. It prints `PASS 7219 independent analytic-grid, asymptotic, monotonicity and simulation checks.` upon success.

The code's random samples support the covariance identities within specified tolerances; they are not a substitute for the proof of global uniqueness, exact fractions or asymptotic limits. The analytic derivation is in `RESULT.md`. No externally generated verification evidence or independent audit is claimed.
