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

Independent exhaustive replay enumerated all 65536 subsets and reproduced cardinality counts (1,16,88,208,228,128,56,16,2) and augmented oriented boundary ranks (1,15,73,135,86,42,14,2) over F101. Rational boundary ranks cannot be smaller, so rational Betti numbers are bounded by the modular ones; the reduced Euler characteristic −7 forces exactly seven rational classes in degree three. Automorphisms fixing zero act faithfully on its four neighbors: for a vertex of weight w, the distances to those neighbors determine its entire support. After translating zero, this exhausts all 384 maps. For a fixed face with c vertex cycles the negative reduced Lefschetz contribution is (−1)^c, including the empty face; the independent replay used this rule and matched every character value, with distribution −3:24, −1:161, 1:188, 3:6, 5:4, 7:1. The translation Fourier weights are 0 with multiplicity three and 7,11,13,14 each with multiplicity one; the latter are transitively permuted, which proves absolute irreducibility. The explicit signed monomial action is a representation and has the remaining trace after averaging out translations; equality of characters over characteristic zero gives the rational identification. Rational averaging on a barycentric subdivision proves the quotient conclusions. Replay of the six subgroup averages gave (3,3,3,0,1,0), in the order of frozen proof §4.

## originality

FAIL

Distinct catalogue records already give the full rational decomposition, its absolute irreducibility, and the all-element character. One even supplies the full integral signed action. The pure A4 quotient rank is mechanically determined by the known character: the identity, three double transpositions and eight three-cycles have traces 7, −1, 1 respectively, so the invariant dimension is (7−3+8)/12=1. This is a coverage finding, not an attribution of priority or provenance.

## value

FAIL

The full B4 invariant of this natural small toroidal complex is scientifically meaningful, but it has already been obtained, even integrally. The new presentation and exact finite replay corroborate it; the subgroup average and the displayed basis formula are immediate uses of the known character or integral generators. No surviving scientific gain over those records is identified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
