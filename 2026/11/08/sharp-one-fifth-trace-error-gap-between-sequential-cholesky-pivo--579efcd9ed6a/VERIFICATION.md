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

The exact formulas for both pivot laws, their Nyström residual traces, and the sharp polynomial identity are independently exercised by `verify.py` (requires `sympy==1.14.0`). The bundled `verify_output.txt` records 682 passing exact assertions on symbolic identities, rational positive-definite matrices, and the rational approximation to the sharp boundary family.

**Proof versus computation.** The continuous all-input inequality and strict positive-definite upper bound are established in `RESULT.md` by a matrix-projector triangle inequality, monotone dispersion, and factorization. The finite grid in the verifier is only a cross-check and makes no exhaustiveness claim. The result concerns mathematical exact arithmetic; finite-precision Cholesky and DPP implementation details were not evaluated. Scientific precedence remains subject to independent assessment.
