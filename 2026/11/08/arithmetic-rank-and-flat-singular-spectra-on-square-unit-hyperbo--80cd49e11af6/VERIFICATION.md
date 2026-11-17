---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Writing K(v)=exp(2πic(v+v^-1)/p²), inversion of columns converts the square matrix into convolution on the abelian unit-square group Q. Its singular values are absolute Fourier multipliers. Every unit square decomposes uniquely into Teichmueller representative w_x of x in Q0 and 1+ps, and summing principal-unit phases enforces stationary index a=c(x-x^-1) modulo p. Fibers are singleton or {x,-x^-1}; if two distinct points occur, their phase ratio has primitive p² order because x+x^-1 ≠ 0 modulo p, while tame character factors have order coprime to p, preventing cancellation. Thus multiplier nonzero iff a lies in stationary image, count h times image size. Involution J(x)=-x^-1 has no paired square fibers if p≡3 mod4, fixed points precisely if p≡1 mod8. This gives all three rank cases and flat positive singular values p for p≡3 mod4. Independent direct SVD checked p=3,5,7,11, including flat p values; finite cases do not prove all primes.

## originality

PASS

Kelmer (2008) Proposition 2.1 proves closely related stationary-phase expansions for multiplicative twists over the *full* units; it does not state self-principal Fourier rank on the index-two unit-square subgroup nor the resulting modulo-eight orbit and flat-spectrum classification. Earlier Resultary reciprocal hyperbola theorem is over Fp rather than Z/p² and indexes all nonzero units; the two contexts cannot be reduced by mod-p projection. The new contribution is the subgroup restriction/count and singular-value consequence, with historical equivalence risk noted.

## value

PASS

The unit-square hyperbola modulo p² is the first natural prime-square, index-two arithmetic subset for a Fourier inversion problem. Its sharp congruence-class rank changes and exact partial-isometry phenomenon reveal identifiable and lost sampling modes, beyond general Kloosterman bounds. It is a motivated complete prime-family classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
