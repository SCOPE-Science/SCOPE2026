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

Run `python3 four_knot.py` with the Python 3 standard library. It computes the exact 30-site rational spline transfer, verifies the explicit input pair through primal-dual KKT inequalities, and checks the boundary-layer arithmetic. The proof of the general asymptotic lower bound uses affine least squares and a continuum normal-equation limit, not finite experimentation. Independent audit has not been performed.
