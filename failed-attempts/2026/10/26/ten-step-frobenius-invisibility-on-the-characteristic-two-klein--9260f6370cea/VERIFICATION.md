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

The partials are the squares of the preceding coordinates and have no projective common zero. Weak Lefschetz and duality give the four Tate groups, and the coefficient of H³ in (1+H)^5/(1+3H) is −2. Since the degree is three, Euler characteristic is −6 and b3=10. The order-eleven diagonal map preserves the cubic, has distinct weights, and each nonidentity power fixes exactly five coordinate points. The tangent spaces have no fixed direction (all ambient tangent weights are nontrivial), so every local fixed-point contribution is one. Lefschetz and the trivial action on the Tate groups give trace −1, hence ten nontrivial one-dimensional character spaces and no trivial one. Galois sends the map to its square, so Frobenius permutes those spaces by 2 or its inverse; 2 has order ten modulo 11. A weighted ten-cycle has characteristic polynomial U^10−c and determinant −c. Taking the fifth exterior power of the alternating pairing shows that the determinant is (2³)^5, so c=−2^15 without any sign ambiguity. The trace formula then gives all counts, including the positive correction 327680 at n=10. As independent finite corroboration, exact additive-character sums of the binary quadratic forms Tr(tF) confirm n=1–20, including 1075119105 at n=10. The cohomological proof—not that computation—establishes the universal assertion.

## originality

FAIL

Debarre–Laface–Roulleau give the same cyclic cubic in their equation (17) and explicitly compute P3(X over F2,T/2)=1+2^5T^10 in §4.5.2. Substitution T=2S yields exactly 1+2^15S^10, not just geometric similarity over an algebraic closure. The frozen polynomial, zeta function and point counts are therefore already covered.

## value

FAIL

The fixed arithmetic form is a natural example and the proof by cycling character spaces is concise, but the finding claims an exact invariant already explicitly computed. The point counts and delayed first discrepancy are routine consequences of that known polynomial, while the character decomposition and cycle deduced from the geometric trace and cyclotomic action do not supply a separately established new valuable outcome here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
