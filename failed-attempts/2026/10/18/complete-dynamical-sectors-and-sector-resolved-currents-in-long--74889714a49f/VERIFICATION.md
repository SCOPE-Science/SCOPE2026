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

The marked-coordinate lift is bijective with ordered headways and the position of particle 0. Allowed jumps conserve each residue and the marked phase modulo gcd(L,I). With at least one positive bare rate, one can transport quanta between any ordered gap sites along the corresponding directed cycle. Circulating a single quantum restores the composition and shifts the mark by ±I, yielding all allowed phases even in one-way dynamics. In the product measure, multiplying by a donor rate removes one copy of the donor quantum in the weight; the matched incoming flux has the same product, separately for each direction. The expected donor rate is the coefficient ratio. Stationary conservation equalizes all individual bond currents; summing their signed crossings multiplies the net jump rate by I. Frozen vectors exist iff H≤N(I−1), active ones iff H≥I. As a separate check, an occupied-site (not gap-transfer) implementation tested 296 generators, 25,456 marked states and 14,968 classes at 3≤L≤8, 2≤N≤4, and all 1≤I<L, with one-way, unequal and equal rates. It tested exact weighted balance and current at each bond separately. Replay: python3 /workspace/branches/audit-4.py.

## originality

FAIL

The distinctive marked-class partition, class size, phase-uniform product law, coefficient-ratio physical current and frozen/flowing coexistence are materially covered by the distinct Resultary record d53436c26fea. Its formal mobile-class statement requires positive rates in both directions and I≥2, but its proof exhibits the one-direction quantum circulation and direction-wise balance. Replacing each reverse gap transfer by N−1 forward transfers and then correcting the mark by the exhibited full circulation is a mechanical extension, not a separate sector result. For I=1 the same computation has zero residues and d=1, recovering a single active class. This is a finding of present scientific coverage, not a claim that the separately archived November entry predates the October record or evidence about who first derived the result.

## value

PASS

As an all-size structural theorem the sector labels explain which initial states can transport, and the class-conditioned law and current answer what a global stationary mixture cannot. Coexistence at the same density is a sharp physical consequence. The scientific utility of that theorem is real, but it is not a distinct contribution of the frozen record under the originality assessment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
