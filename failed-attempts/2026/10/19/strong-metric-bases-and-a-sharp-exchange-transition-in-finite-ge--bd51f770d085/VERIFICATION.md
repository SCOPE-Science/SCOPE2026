---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The projection axiom and its dual give distances 1/3 across the two shores and 2/4 between distinct vertices on a shore. All distance-four pairs are mutually maximally distant. At distance one another incident neighbor gives distance two; at distance two choose a neighbor away from the common incidence to give distance three; at distance three choose a line through the point other than its unique line meeting the given line to give distance four. The standard cover argument uses at least one endpoint of each mutually maximally distant pair, not literally both as one sentence in the proof says; the following argument and all formulas use the correct vertex-cover convention. A maximal geodesic extension proves sufficiency. There are exactly two components: for any two points the union of their closed collinearity neighborhoods has size at most 2[1+s(t+1)], less than (s+1)(st+1) for s,t≥2, so a point noncollinear with both exists; the dual gives line-side connectivity. Pairwise collinear points lie on a line by unique projection, and dually pairwise intersecting lines lie in a pencil. Taking complements of independent maxima gives the basis formula and count. Changing line costs s or s+1 and changing point costs t or t+1, with the frequencies in the claimed factors from counting through the incident points/lines. Below max(s,t) one coordinate is fixed on every component; at max(s,t) no two-coordinate move is allowed and the single-coordinate factors are as stated. Noncomplete factors have diameter two by projection, giving the asserted product diameters. The supplied finite-check sources and recorded results were read but not executed; the axiomatic argument, not those cases, establishes the result.

## originality

FAIL

A distinct available Resultary record covers the basis classification and exchange transition at identical scope, and its coordinate costs mechanically imply the additional fixed-basis enumerator. This is a coverage finding, not a date-based priority or provenance finding.

## value

FAIL

The exact reconfiguration transition on quadrangle bases is a worthwhile question, but that transition and its main structural answers are already demonstrably covered in an available broader theorem. The extra cost polynomial is then simple multiplication of already known coordinate costs with standard degree counts. No independently useful unknown remainder is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
