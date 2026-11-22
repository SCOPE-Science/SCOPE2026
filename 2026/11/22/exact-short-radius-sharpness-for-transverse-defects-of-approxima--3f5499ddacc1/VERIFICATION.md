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

The complete analytic proof is in `RESULT.md`. It checks all six ordered pairs of the three pieces, with the exact epsilon-isometry inequalities, the limiting direction and both boundary radii. The cited published theorems supply the universal upper bound and the long-radius attainment; the new conclusion does not follow from a finite experiment.

`CHECK.py` is an independent numerical stress test of the explicit formula for normalized epsilon one. Run `python CHECK.py` with Python 3 and NumPy. The check samples 400,000 pairs across 80 positive short radii, including small, threshold-adjacent, boundary and large-domain points. Its successful output is `SHORT_RADIUS_EPSILON_ISOMETRY_DIAGNOSTIC_OK 400000`. Floating-point tolerance is 2e-8 and therefore this is supplementary evidence only, not formal or exhaustive verification.

No independent mathematical audit has been performed. The literature comparison credits Turnšek (2026), Theorems 1.2 and 1.3, and isolates new attainment for 0<r<2epsilon. An unindexed earlier equivalent construction is a remaining priority risk.
