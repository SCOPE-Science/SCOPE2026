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

# Reproducibility and mathematical verification

The exact continuum proof is in RESULT.md. The standalone file `checks/dice_volume_check.py` uses only the standard Python library. Run it from the root of this extracted package using `python3 checks/dice_volume_check.py`; the success marker is `DICE_WEIGHTED_VOLUME_AND_SHARP_STABILITY_CHECKS_PASSED`.

Its independent computation replaces each planar disk with a regular inscribed polygon and uses the finite zonotope determinant volume formula for the Minkowski sum. The test covers equal positive radii, unequal positive radii, and configurations with one zero radius. Inscribed polygonal volume approximants converge from below toward the analytic formula. A separate test checks the volume deficit against the proposed sharp quadratic coefficient at six configurations, including both analytic equality types. Finite computations corroborate rather than certify all nonnegative radii.

The hypergeometric constant is represented by an absolutely convergent series. The numerical script computes a finite truncation and deliberately prints an approximate value; the precise definition and global analytic bounds are in the proof. No external verification or independent audit has been performed.
