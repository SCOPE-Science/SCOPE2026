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

# Reproduction and scope

Run `python verify.py` with `sympy` available. The verifier constructs the square-root matrices, applies the exact frozen Sylvester solve twice, checks the closed forms and the characteristic polynomial of the derivative on all real two-by-two matrices, and validates the rational witness. Assertions use symbolic simplification or exact rational arithmetic; a small deterministic parameter sweep provides only additional consistency checks.

The all-parameter claims are proved in RESULT.md; finite checks alone cannot certify a universal or asymptotic statement. The original method uses the frozen operator \(\mathcal L_Z\) at every update. No claim is made about an implementation in mixed precision or about a numerical Schur approximation. Independent audit: not performed.
