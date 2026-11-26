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

Independent exhaustive replay uses the chosen set of spokes to cut the two 12-cycles into paths. Each even path has one perfect matching, each odd path has none, and an uncut cycle has two options. This generates the 120 matching masks without duplicates by a different decomposition from the frozen scripts. Pairs of internally disjoint equal-length paths catalogue the 4-, 6- and 8-cycles: 0, 12 and 54. All 7140 matching-pair differences were tested against the cycle catalogues; when the difference is a single cycle it alternates automatically. The frozen certificate's matching, cycle and adjacency data agree entrywise. Complete distance-layer searches recover 192 hexagon edges, components 57, 18, 18, 18 and nine singletons, and radius and diameter 6 for each nonsingleton. The 414 additional edges give 606 total, connected, with radius 4, diameter 6, eccentricities {4:96,5:18,6:6} and degree distribution as stated; the hexagon degree distribution also agrees. The graph is bipartite by opposite parity conventions on its two layers. The six-cycle cells meet twice at every edge with triangular vertex links and consistent opposite face orientations; the connected closed orientable surface has Euler characteristic 24−36+12=0. This verifies the facial interpretation and the sharp length cutoff.

## originality

FAIL

A distinct published catalogue record establishes the same sharp threshold by the stronger fact that octagons alone connect the entire matching space. It supplies the same hexagon fragmentation and separately computes both edge layers on the identical, common indexed matchings. Its stated octagon-only eccentricity profile is not the frozen combined profile. But its supplied exact-layer construction materially covers the combined statistic: set A[i]=build(6)[i] ∪ build(8)[i], then apply its existing neighbor counts and distance routines. This is a mechanical union and tabulation on already specified exact adjacency data, not a new threshold or reconfiguration result. This comparison does not establish priority from dates.

## value

FAIL

The first cutoff for connectivity on a standard toroidal hexagonal graph is a worthwhile invariant. It is already settled by octagon-only connectivity and hexagon-only fragmentation. The remaining difference is the standard component and distance census of the union of the two fully available layers, which by itself is a mechanically implied finite bookkeeping refinement, not a surviving independently useful unknown invariant under the review standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
