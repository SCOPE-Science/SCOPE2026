---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Finite verification

The Python implementation enumerates proper colourings by a backtracking search on the explicitly listed eleven original edges, tests every possible one-coordinate recolour, performs full-state breadth-first searches from every colouring and canonicalizes all colour permutations. The independent C++17 implementation constructs the complementary subdivided-utility-graph representation, scans all \(k^7\) named-colour words, constructs every legal move using base-\(k\) arithmetic and runs all-source breadth-first search.

Run these complete source programs with the commands in `RESULT.md`. Both were executed after extraction from the output package and each reported the same 384/5040 state counts, 528/22560 undirected recolour moves, eccentricities universally 13/10, degree histograms and complete pair-distance distributions. The isomorphism between the two representations is explicitly given in `RESULT.md`.

**Logical limits.** Breadth-first search is exact for the enumerated finite graph because every legal vertex and edge is enumerated, with no cutoff, pruning of reachable states or timeout-based assumption. The check does not establish an infinite family result, novel connectivity, or absence of an unindexed older exact table. Independent scholarly validation was not performed.
