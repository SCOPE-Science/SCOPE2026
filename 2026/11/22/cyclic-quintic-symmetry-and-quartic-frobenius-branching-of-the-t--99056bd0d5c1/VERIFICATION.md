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

The certificate `verify_excessive_aut.py` was executed against both original finite-field models. It enumerates all rational projective automorphisms of their nonsplit quadrics, checks cubic preservation as an exact coefficient identity, verifies group generators, smoothness over algebraic closures using Jacobian-minor Gröbner ideals on all affine charts, and verifies pointlessness over each base field. Output is `EXCESSIVE_GENUS_FOUR_AUTOMORPHISMS_VERIFIED`.

The genus-zero quotient, tame branch count, and Frobenius transitivity are established in the mathematical proof; a finite check by itself is not a substitute for Riemann--Hurwitz or the irreducibility argument. The certificate uses Python with SymPy.
