---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Simultaneous matched-index permutations and part interchange give exactly three pair orbits. The grounded diagonals remain d=n−1+t, and connectivity gives positive definiteness. The bipartite adjacency spectrum pairs ±singular values with extra zeros; the same-part block has Gram matrix h²I+(n+2h)J on the smaller side, h=t−1. For matched leaders use J+hI on n−1 indices, and for unmatched leaders split differences among the common matched indices from the two-dimensional compression. This verifies the three spectral costs. Independently clear denominators using K=n+2h, L=2d−1, H=2d²−n, P=KH, A=d²+L+2h. The matched numerator is 4n²d⁴K²−2n²d²K²L−2n²K²L²−(n²−4)d⁴L²+n(n−2)d²KL². The unmatched-minus-same numerator is 4d⁴(A²−2P)−2d²AP−2K²H²−d⁴H²+d²KH². Exact integer coefficient multiplication in (n−3,t) and (n−3,t−1), respectively, agrees with all displayed coefficient rows of CERTIFICATES.md. Descartes, the negative constant and the positive value at 1/2 prove uniqueness and direction of the switch. The latter numerator proves strict unmatched domination by same-part at t≥1; for 0<t<1 entrywise nonnegative inverse Neumann series strictly increase at an affected entry from matched to unmatched, and the trace of the inverse square is the sum of squared entries. Orbit sizes give n, n(n−1), n(n−1), hence n² minimizing pairs at equality. At 1/2, Q=6n⁴−18n³+O(n²) and Q'=8n⁷−28n⁶+O(n⁵), verified by coefficient arithmetic. Q has degree at most seven in n, bounding its second derivative uniformly on a fixed t-neighbourhood. A bracket of radius O(n⁻⁵) around the stated two-term root follows by Taylor signs and uniqueness. The J1 version gives the stated cubic and scale; the unmatched-minus-same J1 difference also simplifies to [d²(n−2)+2nK]/(dKH)>0. Independent exact arithmetic at n=3,t=9/20 recovered both signed rational differences; direct exact grounded-matrix evaluation across all 15 pairs corroborated the witness. Replay from RESULT.md and the two cleared polynomials above is all-size; bundled script and notes were inspected, not executed. Scope is positive matching weight, unit off-matching conductance, two perfect leaders and the combinatorial grounded matrix, not general second-order dynamics.

## originality

PASS

The exact same-family J1 cubic and orbit optimizer classification are credited. The J2 threshold and its cubic-order boundary layer are distinct. The inspected general leader-coherence formulas and nearby exact J2 graph classification do not imply this J2 sign comparison, polynomial root, or separation scale.

## value

PASS

On an infinite tunable network family, the result chooses all minimizing leaders including weights of ties and rules out one orbit. The contrast with the same family's established first-power threshold shows the choice of coherence objective changes actual optimal leader locations, on an interval with a quantified nonzero width, not merely the objective's numerical value. The independently verified small rational example makes that distinction directly testable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
