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

## Reproducibility

Run `python verify.py` with a Python installation that includes SciPy. The checker uses the exact eight phase definitions as displayed in the source equations, checks their analytic derivative identities by independent centered differences, evaluates the two exact periodic mean variations, and computes finite inverse counts on four growing input windows. A successful replay prints `VERIFY_OK`.

The periodic inverse counts are numerical diagnostics based on bracketing the stationary points on a mesh; they are **not** exhaustive symbolic root certificates. The full infinite assertions, error terms, and critical-state statements follow from the analytic proof in `RESULT.md`, not the finite checks.

## Review scope

The full primary study was read, including its equation tables, and the new mixed-model asymptotics were compared with the previously available quadratic-only calculation and related published inverse-valence results for different maps. Independent mathematical audit and comprehensive literature priority verification are not yet performed.
