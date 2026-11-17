---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The fold interval I_(n−t−1) covers every Markov cell while all other branches are isometries forming one forced chain of length n−2; the first-return loop lengths are 1..n−1. det(I−zA)=1−sum_(r=1)^(n−1)z^r by the renewal identity, and every admissible closed path hits the strict folding contraction. The endpoint knot orbit is a primitive n-cycle with unique itinerary, eliminating physical overcounting. Standard Perron-Parry theory gives entropy, uniqueness of maximizing measure and iid lengths rho^(−r). Independently assembled transition matrices for ALL coprime steps n=3,...,9 and verified exact integer characteristic polynomials. Finite checks corroborate the analytic Markov proof.

## originality

FAIL

FAIL: a November 1 complete same-map theorem already states identical coprime zeta, entropy and graph, and by standard Möbius inversion/Parry renewal theory yields the rest; the November 8 title obscures prior implication, despite the new proof being correct.

## value

FAIL

Although the exact physical zeta and first-return law are mathematically natural, a Nov 1 earlier theorem fully specifies the identical map, complete coprime zeta/entropy and exact renewal hub graph. Primitive counts follow mechanically from that existing zeta, and iid return lengths with rho^(−r) is the routine Parry Markov cylinder computation on that explicit graph. Nothing independently motivated and non-implied survives; a reformulation is not a new value-bearing finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
