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

# Reproduction and limits
Run `python verify.py` with Python 3 and SymPy. The checker executes direct exact-algebra tests for the centre graph through total degree two, absence of a quadratic slow term, cubic coefficient, source equilibrium quadratic, Puiseux saddle coordinates, Jacobian leading determinant and stable eigenvalue, and positivity of the normal-form coefficient on three rational parameter examples. The executed check returned `VERIFY_OK`.

The proof of the singular limit uses analytic center-manifold and stable-fiber estimates and two-stage first-hitting-time comparison. No finite calculation or stored trace is treated as an infinite-time certificate. The cutoff and the equality-amplitude boundary case are excluded as stated in RESULT.md. Independent audit was not performed.
