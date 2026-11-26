---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Independently enumerated the polar normals directly in Z[√5] using the cube corners (±2,±2,±2) and cyclic permutations of (0,±(1+√5),±(√5−1)). Dot products with the scaled given vertices verify 20 distinct supporting triples; these normals have length √12. Cauchy's formula therefore gives B(u)=(1/2)max_v u·v for the 1024 signed sums of ten polar representatives. The independent exact calculation gave 18 squared-norm levels, with leading pairs (168+72√5, count 20) and (168+56√5, count 60), one top ray per face normal. It verified 30 adjacent-face edges, exactly 6 opposite-sign pairs at every top ray, all off-diagonal normal cosines ≤√5/3, minimum absolute cosine ≥1/3, and both strict cap inequalities. The same calculation is replayable in /workspace/branches/audit_icosa.js with Node; uploaded checker inspected, not run. Hence for t>B1 the maximal rays give all caps, separated and in fixed sign chambers, and the cap area is 2π(1−t/B+). At B1 additional sign sums can add only isolated directions; B+ has only the top directions, of area zero. Indeed the computation found the 60 second-tier radial directions strictly outside all B1 top caps, so slightly below B1 there is positive extra area and this upper band is sharp. The cap sum gives 10(1−t/B+), and 400B1²<361B+² proves the band contains strictly more than half the mass. Facet-normal and silhouette assertions do not require treating the isolated endpoint directions as hexagons. Uniformity of conditional cap label/orientation holds for the positive-mass upper events, not for conditioning at B+.

## originality

PASS

Pass is for the explicit icosahedral upper band, its exact majority mass and its hexagonal mark, not Cauchy's formula, generic spherical cap tails, or a general polyhedral density method. The strongest same-object nearby records give side counts, area-weighted moments, variance, or a different metric. Abas gives a genuinely applicable general theorem after passing to the projection body, but applying it does not supply the required icosahedral normal-cell geometry, breakpoints, numerical band mass, or silhouette mark. Related same-day solid-specific cap laws are not discarded on date grounds; the examined tetrahedral one differs and the dodecahedral full record remains an access risk, distinct from the evidence against equivalence of the solids' projection bodies.

## value

PASS

This is an exact distributional invariant for a canonical solid under natural Haar orientations. The explicit band is not merely an infinitesimal endpoint expansion: it contains over half the orientations and has a sharp cutoff, constant density, and an exact link to the six-sided projection type. The band provides computable probabilities and marked orientation sampling unavailable from the known silhouette counts and first two area moments. The finite certificate resolves the crucial full-cap and incidence conditions; it is not a numerical census promoted to a full distribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
