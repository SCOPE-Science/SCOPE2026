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

Run `python artifacts/verify.py` with Python 3, NumPy and SciPy. The script compares an exact rational integrated polynomial against an exact binomial sum for 840 parameter profiles; it also independently enumerates all integer tight-spanning candidate vertices in nine small rooted polars and numerically computes their convex-hull volume.

Expected successful output: `SPLIT_LIPSCHITZ_POLAR_VOLUME_CHECKS_PASSED exact_profiles=840 independent_hulls=9`.

The hull comparisons are numerical at a stated relative tolerance; the rational formula tests are exact. Analytic proofs of the full infinite range and Gaussian asymptotics are in `RESULT.md`. These experiments do not constitute an exhaustive search of the literature or an independent mathematical audit.
