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

The proof in RESULT.md gives an integral presentation of first regular GLMY path homology and an all-parameter separation of short additive relations. The attached `verify.py` is a standalone Python 3 integer-arithmetic corroboration, using fraction-free determinants and enumeration rather than field-only rank testing.

The program verifies the eight-point block's fifth-minor gcd is one and its sixth-minor gcd is two, yielding Smith factors \(1,1,1,1,1,2\). It also enumerates every short relation for \(r=1,2,3,4,5\), checks that there are exactly \(6r\), checks that none is a triangle or a cross-block collision, and prints the predicted first integral homology invariants. The mathematical proof, not the finite test range, establishes all \(r\ge1\) and all \(n>2\max S_r\).

Scope: first integral regular path homology only. No external independent mathematical validation has been performed. Finite checks are exact but are not substitutes for the uniform proof.
