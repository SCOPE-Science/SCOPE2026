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

The standalone `CHECK.py` requires SymPy (see `requirements.txt`). It reconstructs the beta-moment coefficients, the center curvature expression and its exact transverse derivatives, the integer-exponent curvature formulas, the weight-four metric and numerator, and the reciprocal-polynomial root-count inequalities. Execute `python CHECK.py`; a successful run prints the exact symbolic PASS statement.

The infinite-parameter analyticity and boundary-limit assertions rely on the displayed analytic proof rather than finite checks. The root near 0.0175975033598718 is isolated numerically only after the two-positive-root proof. No independent audit is claimed.
