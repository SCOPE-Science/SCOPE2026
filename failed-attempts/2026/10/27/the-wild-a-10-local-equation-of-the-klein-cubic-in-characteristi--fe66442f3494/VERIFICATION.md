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

A zero coordinate at a projective critical point forces the preceding coordinate to vanish and hence forces all five to vanish. With x_0=1, the first three gradient equations give b=-1/(2a), c=a^3, d=-1/(8a^5) (a is a unit), and the fourth imposes a^11=3 or (a-3)^11=0. The restriction f=5a/8+1/(64a^10) has numerator 40a^11+1 over 64a^10, hence vanishes in the gradient quotient in characteristic 11. This gives the sole support [1:3:9:5:4] and the intrinsic quotient of length 11. The transverse Hessian in a,b,c has determinant 7(80-49)-36*8=-71=6 modulo 11, and d'(3)=5/(8*3^6) is nonzero. Thus d parametrizes the formal transverse critical section. Translating that section to zero leaves a quadratic expression in the transverse variables with invertible symmetric coefficient matrix over the power-series ring; congruence and formal square roots reduce it to three squares, with an invertible transverse linear part. On the section a=3(1+u) gives residual 6(1+u)+5/(1+u)^10=6u^11(1+u)/(1+u^11). Dividing by its unit factor and rescaling the squares proves the complete local ring (contact, not right equivalence). Its Tjurina algebra imposes the three transverse coordinates and u^11; the u derivative vanishes. The supplied checker was inspected, not executed; these exact identities and the formal argument are independent of bounded computations. The published A2 equation would have length 2, not 11.

## originality

FAIL

The point and its uniqueness were already stated for this cyclic equation. A distinct indexed record gives the identical characteristic-eleven completed contact equation at this point by another critical section. The length-11 Tjurina algebra follows immediately from that equation. The older A2 label is a real conflict, not an equivalent formulation, but all scientific content of the frozen result is demonstrably covered in the inspected sources taken together. The date of the exact matching catalogue entry does not establish historical precedence for the formal equation.

## value

FAIL

The exceptional fiber and its formal type are genuinely motivated, and correcting the A2 label would matter mathematically. However, the exact correction is already present in the distinct indexed normal-form finding and already entails the stated intrinsic length. The frozen alternative calculation does not supply a further invariant, deformation statement, or new consequence beyond that coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
