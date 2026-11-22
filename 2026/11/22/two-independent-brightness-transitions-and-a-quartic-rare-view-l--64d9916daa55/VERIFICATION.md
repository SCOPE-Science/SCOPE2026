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

# Reproducibility and limits

Run `python3 check_bicone.py` in the same directory with NumPy and SciPy installed. The script computes independently projected polygonal convex hulls for a fine discretization of the equatorial circle plus both apices and compares their areas to the exact two-branch formula. It also compares numerical mean areas against one quarter of the analytic lateral surface, checks extremal values over dense orientation grids, differentiates the analytic profile numerically, and tests the critical quarter-power and minimum-latitude bifurcation asymptotics.

The checker passed **432 deterministic assertions** in the stated environment. Its polygonal-hull comparisons are approximations and do not prove complete equality classes, novelty, or a continuum result. The proof of the universal distribution, strict uniqueness, and coefficients is supplied in `RESULT.md` using exact geometric tangent constructions and derivative monotonicity. No independent audit has been performed.
