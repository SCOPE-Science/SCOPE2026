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

# Verification

Run `python CHECK.py` in Python 3 with no third-party dependencies. It independently solves the natural-spline tridiagonal linear system, obtains extrema from each cell derivative polynomial, and compares full total variation with the closed formula. It also checks subcritical convergence, critical linear slope, and the supercritical normalized constant. The checker has been executed successfully.

An independent earlier check compared the explicit knot curvatures and variation with SciPy's `CubicSpline(..., bc_type='natural')` on eight grading ratios and several knot counts, with agreement within numerical tolerance. These are finite computations and not a proof of the all-parameter asymptotic theorem. The analytic derivation is in `RESULT.md`. Independent mathematical audit has not been performed.
