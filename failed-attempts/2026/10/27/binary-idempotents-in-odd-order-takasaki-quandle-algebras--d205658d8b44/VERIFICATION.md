---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The auxiliary associative group algebra is commutative and coefficient squaring over F2 leaves coefficients unchanged. Ordinary x^*x^2 therefore has at a^{-1}b^2 exactly the contributions of the Takasaki square. Odd group order permits Fourier inversion over a splitting field, and evaluation at the successive squarings of a character is equivalent to one degree-d finite-field coordinate. Inversion commutes with squaring. On a nontrivial stable orbit it acts by the sole nonidentity involutory rotation, the half-turn, since no nontrivial odd-order character equals its inverse. Thus the local choices are zero and the kernel of the norm to the half-degree subfield, giving 2^{d/2}+2. Inversion interchanges the two other types of orbit in inverse-linked pairs, for which the equations give (0,0) or xy=1, totaling 2^d. The trivial character gives two choices, including when A is trivial. The cyclic examples agree with the reciprocal irreducible degrees (e.g. for C_15 the order-3 and order-5 parts contribute 4 and 6 and the order-15 part is a paired contribution of 16). For C_3×C_3 the four nontrivial orbit pairs of characters are each one stable orbit of size two, giving 512; directly, the product is commutative in exponent three and all cross terms cancel.

## originality

FAIL

The cyclic classification is explicitly covered by earlier work, and its local orbit classifications mechanically give the stated noncyclic product as well. This finding is correct but the extension does not introduce a new local case or an additional coupling. The conclusion is based on the prior cyclic theorem and its proof, not on inferring priority from the later all-abelian record or treating an inaccessible source as negative evidence.

## value

FAIL

Binary Takasaki idempotence is well motivated and the involution packaging is a readable short proof. However, the new-looking noncyclic count is a multiplication of already classified independent generator blocks, and the frozen finding establishes no new arithmetic constraint, structure, or exact invariant beyond that mechanical implication. It is useful exposition, not a standalone distinct contribution under the review standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
