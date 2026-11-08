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
The geometric projection formula was compared with direct convex-hull volume computations for regular simplices in small dimensions. Crossed-face counts were independently enumerated by checking every vertex subset. Normalized shadow means and second moments, and the mean vertex deficit, were compared against simulated Gaussian normals. The asymptotic covariance matrix was numerically checked in dimensions 200 and 1000.

Run `python verify.py` (Python 3 with NumPy and SciPy installed). A deterministic pseudorandom seed is set in the script. It reports 387 assertions, including 360 direct geometry/face assertions, 21 moment comparisons, and six covariance checks. These finite checks are supplementary: the infinite-dimensional assertion uses Gaussian asymptotic linearization and a bivariate central limit theorem, not finite testing. The standard empirical-CDF local equicontinuity step is a mathematical hypothesis of the cited standard limit theory, with its application explained in RESULT.md.

No independent mathematical audit has been performed. The record makes no external certification claim.
