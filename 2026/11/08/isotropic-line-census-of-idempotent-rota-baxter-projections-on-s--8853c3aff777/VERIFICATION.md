---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For nonzero symmetric bilinear B on a two-space V over any field, radical m=V+kz of A=k1+V+kz has m²=kz and m³=0. The weight-minus-one RB identity with P²=P is equivalent to image and kernel each closed under products. Any subalgebra containing an element with nonzero scalar residue contains 1 by the invertible element’s minimal polynomial; hence exactly one summand is unital. Radical subalgebras admit nontrivial complementary line-plane pairs only if the line lifts an isotropic projective direction and the plane contains kz with distinct projected direction. For Fq each isotropic direction gives q lift lines and q complementary planes, yielding N=h_B q²; two orientations and complementary ranks give polynomial 1+(1+N)T+2NT²+(1+N)T³+T⁴. Characteristic-two alternating/nonalternating and odd split/anisotropic/rank-one isotropy are handled explicitly. Independent exhaustive direct 2^16 linear-map checks over F2 for three distinct forms reproduced rank distributions.

## originality

PASS

PASS, qualified. Idempotent RB operators as subalgebra projections are a known general equivalence (Jian 2013 and prior). The submitted novelty is not that equivalence: it is the complete all-field radical splitting criterion and finite-field rank distribution sensitive to projective isotropy, including degenerate forms and char two. The closest previously indexed finite local quadratic-algebra result instead counts averaging projections, which obey different image/kernel identities; spin-factor and square-zero radical results have different algebra objects or weights. No exact pre-existing isotropic RB rank polynomial was found.

## value

PASS

PASS. Exact classification of idempotent weight-minus-one RB maps on natural four-dimensional local Hilbert-type-(1,2,1) algebras is an intrinsic and arithmetic invariant. The count distinguishes anisotropic, split and alternating multiplication forms despite identical Hilbert dimensions and has a characteristic-two degree jump. This gives a complete small local-algebra test case beyond textbook projection equivalence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
