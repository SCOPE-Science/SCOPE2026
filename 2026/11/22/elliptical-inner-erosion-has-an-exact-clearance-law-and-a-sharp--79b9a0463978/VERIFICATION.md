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

# Verification record

The result has an analytic proof of the full distribution and threshold. To reproduce numerical checks, run `python checker.py` with Python, NumPy, SciPy and mpmath. The script (1) evaluates exact support-area and perimeter integrals at high precision, (2) independently intersects sampled ellipse-support half-planes with a convex-hull algorithm and compares their areas on both sides of the curvature threshold, (3) tests the asymptotic area and perimeter coefficients, and (4) checks active-arc curvature bounds over three additional aspect ratios. Tolerances and the test list are visible in the script.

Numerical tests are finite diagnostics only: they do not establish the functional identity for all possible semiaxes or radii. All-parameter correctness rests on the support-envelope argument and local Taylor expansion in `RESULT.md`. Historical-coverage and priority limitations are detailed in `REVIEW.md` and `AUDIT.json`. No external or independent mathematical validation is claimed.
