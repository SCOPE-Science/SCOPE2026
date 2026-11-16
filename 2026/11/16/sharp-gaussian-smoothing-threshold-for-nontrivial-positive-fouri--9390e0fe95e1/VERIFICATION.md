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

The proof is an exact finite-mixture conditional-variance calculation followed by global one-dimensional optimization. The attached `CHECK.py` provides standalone algebraic consistency checks and approximate display of the unique root. Its numerical search does not prove uniqueness; monotonicity and all tail regimes are proved in `RESULT.md`. External independent validation has not been performed.
