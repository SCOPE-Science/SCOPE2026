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

The standalone Python checker `tools/verify.py` executed successfully with the Python 3 standard library and reported 4,812 deterministic exact-rational tests over sample sizes three through fourteen. The checks directly verify reconstruction, inverse fiber parameterization, alternating-balance constraints, and the Jacobian determinants with exact rational arithmetic.

The general theorem is proved by uniform Dirichlet spacings and an invertible or one-dimensional-fiber change of variables, depending on parity. Tests do not certify infinite statements. The density is specified relative to different coordinate measures in odd and even cases and is not an ambient density in even order. Source priority is qualified and independent audit has not been performed.
