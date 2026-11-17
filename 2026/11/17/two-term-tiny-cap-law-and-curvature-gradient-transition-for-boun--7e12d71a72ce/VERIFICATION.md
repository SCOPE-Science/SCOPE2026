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

`cap_checker.py` is standalone with Python 3 and `mpmath`. It evaluates exact cap areas through high-precision Green-theorem integrals on analytically parameterized closed ovals and checks the truncated expansion and its seventh-order residual behavior. It also integrates the curvature-gradient energy independently of the closed form and tests the circle probability with its exact inverse-sine area equation.

Command: `python cap_checker.py`. Observed terminal marker: `SMOOTH_CAP_AREA_CHECKS_OK`. The analytical proof in `RESULT.md` establishes the infinite statements, not the spot-check program. The evidence does not include an independent mathematical audit or historical-priority certification.
