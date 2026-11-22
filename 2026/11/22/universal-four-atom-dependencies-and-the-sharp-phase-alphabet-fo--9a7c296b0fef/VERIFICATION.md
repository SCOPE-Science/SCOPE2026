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

# Exact verification and limits

The standalone script `verify_klein_gabor.py` enumerates all 1820 four-atom sets, recomputes every determinant polynomial by its 24 signed monomial terms, and compares its identically-zero condition with the symplectic predicate for all sets. Exact integer Bareiss evaluation at the stated nonflat window independently checks all 1820 determinant statuses. The same script exhausts all 441 normalized root-of-unity phase assignments across alphabet sizes one through six, reducing every tested determinant by the appropriate integer cyclotomic polynomial, and checks every four-set and three-set for the seventh-root window. `verify_klein_gabor.out` records the observed counts and final successful status.

`verify_klein_modular.py` independently constructs the sixteen vectors in \(\mathbb F_{43}^4\), using an element of exact order seven, and checks all four-set and three-set ranks by elimination. Its rank table consists of 240 rank-three quartets, 1580 rank-four quartets and 560 independent triples. `verify_klein_modular.out` contains its recorded output. Since a primitive seventh root maps to this element of \(\mathbb F_{43}\), each nonzero minor in that field proves nonvanishing of the corresponding integer-cyclotomic minor in characteristic zero.

These are **complete finite checks** with executable exact code, not samples or floating-point tests. No claim about larger groups, optimal singular values or independently audited priority follows. Scientific status is self-reviewed only.
