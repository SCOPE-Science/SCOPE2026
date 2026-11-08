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

The finite-difference and quadrature comparison is executed with `python verify_exit.py` from the same package. It compares solutions of the backward Dirichlet boundary problem with a separate Simpson quadrature of the exact integral for 12 combinations of barrier strength and offset, also checks three larger-barrier asymptotic cases and 121 positive first-correction values. The expected success output is `VERIFY_OK backward_BVP_vs_quadrature=12 positive_corrections=121`.

The exact identities in `RESULT.md` establish the universal statement. The code only tests a finite grid and floating-point approximations; it does not certify the uniform remainder, novelty, independent auditing, or historical priority.
