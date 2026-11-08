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

# Verification scope

Run `python3 verify.py` using the standalone package. The arithmetic checker verifies the positive-definite near-identity construction by multiplication at three positive values of the parameter, the first nondegenerate third Krylov direction, the exact sign-pattern census for eight signed rows, the noncollision lower bound and four binomial-count probability identities. It reports `VERIFY_OK` when all assertions succeed.

The count for general sketch dimensions and sparsities and the limit of the true condition number are analytic results in `RESULT.md`; checking finite examples alone would not establish them. No independent mathematical audit has been performed.
