---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The constant term of P^n pairs words with equal Parikh vectors and gives the multinomial-square sequence. The correction polynomial (P^3−P(x^3,y^3))/3 is integral by the characteristic-three power identity. An independent exact coefficient replay confirmed all three projected supports Π(QP^d)=dS mod 3. Each coordinate of an exponent of P^d for d=0,1,2 lies between −2 and 2, so only its constant term can pair with a monomial in P(x^3,y^3)^m. Expanding modulo nine then gives A(3m+d)=A(m)A(d)+3md(A(m)−3A(m−1)) mod 9 for m≥1. Modulo three this yields Lucas factorization and hence 3|A(m) for m>0 by iteration from A(0)=1, A(1)=3, A(2)=15. That divisibility kills the correction modulo nine. The m=0 identities are immediate and the digit classification and window counts follow, including the separate zero index.

## originality

FAIL

The entire digit law is a direct prior implication, even though the exact statement was not found verbatim. Delaygue gives ν_3(A(n)) at least the number of nonzero ternary digits. Mellit–Vlasenko Theorem 1 gives F(X)/F(X^3) ≡ F_2(X)/F_1(X^3) mod 9, where F_s truncates F at degree 3^s−1. P's hexagonal Newton polygon has area 3 and six boundary lattice points, so Pick's formula gives only one interior lattice point, the origin. As F=1+3G, the left is 1+3(G(X)−G(X^3)) modulo nine. The right is supported through degree 8 modulo nine: its nonconstant terms are the numerator contribution through degree 8 minus the denominator contribution through degree 6, with product terms zero modulo nine. At X^{3m} for m≥3 this proves A(3m)≡A(m) mod 9. The remaining m=0,1,2 follow directly from A(0), A(1), A(2), A(3)=93 and A(6)=35169. Delaygue gives residue zero at every multiple-nonzero-digit index, and this scaling reduces each single-nonzero-digit index to 1 or 2. This recovers the complete claimed product, classification and counts, not just its zero residues.

## value

FAIL

The residue classification is a natural question, and the self-contained projected-polynomial proof is pedagogically useful, but the frozen contribution is the exact invariant itself. That invariant and its counts follow mechanically from existing congruences with a small seed check; no new general use of the projection or further substantive invariant is established. The presentation alone does not leave a separately supported valuable research claim to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
