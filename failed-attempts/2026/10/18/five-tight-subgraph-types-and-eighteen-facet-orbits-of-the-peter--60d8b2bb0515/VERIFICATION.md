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

Shortest-path molecules are convex combinations of edge molecules, and connectedness gives the nine-dimensional span. After quotienting constants in the polar, active edge differences span exactly when the tight subgraph is connected and spanning. A tight spanning tree forces integer coordinate differences and diameter two bounds normalized labels by 0,1,2. Every edge crossing parity is tight and the crossing graph is maximal bipartite when connected; conversely a connected spanning maximal bipartite subgraph contains all crossings of its bipartition and is realized by the indicator of one part. The five independent sets of size four are precisely the stars of the underlying five-set: a pairwise intersecting edge family without a common endpoint is at most a triangle. The stars and their pairwise intersections identify all graph automorphisms as S5. An independent replay at /workspace/branches/285169ca-5528-4168-9c66-ca026bf95a57/independent_petersen_replay.py tested all 511 nontrivial anchored cuts, all 32768 edge subsets and all 59049 ternary labelings. The logged output verifies all five subgraph rows and all 18 facet representatives and multiplicities, the fibers and histograms, and Burnside totals 600 and 4320. The frozen verify.py was inspected, not run; its cut loop actually tests 510 nontrivial cuts, omitting the singleton shore {0}. Its crossing graph is only a three-edge star with six isolated vertices, so the omission cannot affect the result, and the separate frozen edge-subset loop covers it as well.

## originality

FAIL

The original properly credits the known aggregate 1410. The stronger distinct Resultary record 7e3c90bda400 explicitly lists all eighteen symmetry orbits on the same polytope, with the same representatives up to relabeling and reflection, as well as an additional metric refinement. Its complete list mechanically yields the tight-subgraph and fiber tables by an equivariant projection. This is statement-level coverage, not a claim about discovery, priority or derivational dependence: the catalogue path dates differ, and they do not establish those matters by themselves.

## value

FAIL

The Petersen transportation ball is a natural benchmark and a genuinely unknown exact 18-orbit census would be useful. Given the inspected complete orbit list, however, the remaining tight-edge and fiber displays are immediate finite readouts of already classified data. Convenient alternative tables and the independent replay are useful documentation but do not leave an independently useful unknown invariant in the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
