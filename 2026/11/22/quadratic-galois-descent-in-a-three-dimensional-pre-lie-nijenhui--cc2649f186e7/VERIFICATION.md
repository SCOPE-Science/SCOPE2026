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

Compile and execute `verify_quadratic_prelie.cpp` using any ISO C++17 compiler. It independently checks the defining bilinear Nijenhuis identity, the two matrix equations, the union-of-components classification, and all operator ranks. The local run completed successfully for \(\mathbb F_2,\mathbb F_3,\mathbb F_5\) with irreducible quadratic action and for \(\mathbb F_3,\mathbb F_5\) with split-distinct action. Its expected last line is `QUADRATIC_PRELIE_NIJENHUIS_VERIFIED`.

Run `python3 verify_zeta.py` (standard library only) to check the formal logarithm of the rational zeta function through coefficient six for several field sizes and the symbolic rank-count identities by direct polynomial coefficients. These are exact finite integer checks, not infinite-field or full-scheme certifications.

The proof in `RESULT.md` is required for the complete arbitrary-finite-field statement, quadratic extension parity, and the geometric irreducible-component claim. Scientific verification has not been performed independently outside the stated checks.
