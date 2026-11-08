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

# Exact checks and scope

Run `python3 verification/verify.py` in an ordinary Python 3 environment. It uses only the standard library. The actual execution transcript is `verification/output.txt`.

It checks (a) characteristic-two expansion and all five derivatives of the determinant, (b) the exact Euler relation placing the cubic in the gradient ideal, (c) both local chart presentations in square-zero polynomial arithmetic, (d) transition relations under Laurent substitutions, (e) the Laurent exponent obstruction to a global splitting, and (f) finite Hilbert-function consistency with the complete-intersection formula.

The script is independent of symbolic-algebra packages. The assertions about the entire projective scheme, a regular sequence, and infinitely many possible coordinate changes are proved in RESULT.md; finite samples do not establish them. There is no independent audit certificate or claim of formal proof-assistant verification.
