---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

The actual frozen graph is once-subdivided K5 with 15 vertices and 20 half-edges; Prue–Scrimshaw subdivision applies to three unordered points. A separately implemented exhaustive integral cubical chain reconstruction yielded exact cell ranks (455,1560,1650,520), and every d1d2 and d2d3 coefficient vanishes. A full integer unit-pivot elimination of the actual 1650×520 third boundary has 520 unit pivots and zero residual: im(d3) is a primitive direct summand of C2. Consequently ker(d2)/im(d3) embeds in free C2/im(d3), so H2 is torsion-free. A separate d2 elimination produced 1098 unit pivots and the genuine 23×37 residual with Smith factors 1 and 2, total rank1100, giving rank H2=1650−1100−520=30. Signed cubical chain traces were independently enumerated for all 120 vertex permutations, agreeing with the older known rational S5 character. The d2 factor 2 accounts for known H1 torsion, not H2. These are exhaustive exact calculations on a fixed finite complex plus an invoked topological subdivision theorem, not experimental infinite extrapolation.

## originality

PASS

The frozen original incorrectly treats rational H2 S5 character and complete H1 as novel. Both are precisely pre-covered: the October 18, 2026 K5 unordered-three-point publication gives the identical seven-class rational character, five Specht summands, and Betti rank30; Ko–Park gives integral H1 in a broader graph class. The final REPAIRED claim is strictly the integral torsion-free H2 (a 520-unit-pivot saturated image of d3). Rational homology and ordered particle representations do not detect torsion; the earlier exact K5 character paper explicitly disclaims ruling H2 torsion out. Neither relevant inspected full text nor actual publication search determined the narrowed integral result previously. Historical priority remains best-of-knowledge: other unindexed integer Smith computations may exist, and abstract-only sources are not declared noncovering.

## value

PASS

The natural integer H2 of the first nonplanar complete graph at the first three-particle stage is finer than the existing rational Betti number and S5 representation. K5 already has Z/2 in H1, and recent graph-configuration results establish nontrivial H2 torsion elsewhere, so absence of all H2 torsion is a mathematically motivated precise invariant, not a routine renaming, guessed significant number, or a known-table recomputation. The 520-unit-pivot result gives an exact complete integral answer at this canonical finite case, without claiming a general classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
