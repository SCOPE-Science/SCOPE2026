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

## Reproduction

Run `python verify.py` using Python 3 and SymPy. The script checks symbolic identities for the exact transfer and the conditional norm law, and finite rational examples. The finite examples do not establish the all-step/all-bias theorem; that proof is given in `RESULT.md`. The independent scientific audit has not been performed.

The adjoint cone eigenmatrix used in the universal-bias argument is obtained by the positive resolvent at the spectral radius, and its strict positivity follows from absence of real invariant lines for the elliptic update matrix.
