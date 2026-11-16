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

# Verification and reproducibility

The exact one-zero and antipodal coefficient energies follow from strict Hölder equality for geometric sequences. The jet formula is established by both a dual lower bound and an explicit coefficient vector meeting the value and derivative constraints. The strict monotonicity of its normalized geometric variational objective is proved from the exact stop-loss transform and positivity of second derivatives of strictly convex functions. This is an analytic argument over all geometric indices, not a finite enumeration.

To reproduce supplementary finite checks, extract `CHECK.py` alongside these files and run `python CHECK.py` in an environment with NumPy and SciPy. The script checks explicit phase ratios, finite-mode jet minimization, the Hilbert identity, geometric convex-order sample grids, finite two-node collision, and the exact stop-loss formula against numerically truncated sums. These tests are not a proof of limits, strict monotonicity across a continuum, or uniqueness; those are covered by `RESULT.md`. Independent verification has not been performed.
