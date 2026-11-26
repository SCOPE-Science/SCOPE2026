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

No adjacent pair dominates all five nonempty classes, so a perfect-matchable dominating set has at least four vertices. The three core vertices plus any A or B vertex attain four. With no selected endpoint x0 or x2, domination fails or x1 is unmatched. With just one of x0,x2 and no other core vertex, its matching partner needs the adjacent large class and domination of the other endpoint needs the other large class; either (2,1) or (1,2) then works since A union B is a clique. With x0,x2 only in the core, their respective partners must be in B,A. Either adjacent core pair accepts all two additional large-class vertices, and all three core vertices accept either class for the fourth. The role test gives the same patterns: role 1 requires x0 or x2; if one is the sole selected core vertex the two distinct roles 2 and 3 force both A and B; if both endpoints are selected without x1 they are forced into 1 and 4, again forcing A and B. An adjacent core pair leaves two roles that can be chosen to accommodate AA, AB or BB (the roles of x1 can be adjusted); with three core vertices the fourth may be A or B. This accounts for all thirteen admissible patterns and yields the stated counting polynomial by labelled binomial choices. The partial-transversal theorem gives ordinary basis exchange, hence via exchanges increasing the intersection with the target by one at each step, distance 4 minus the intersection size and greedy minimum-weight basis optimization. The pigeonhole diameter bound is tight: the exhibited bases use a union of all vertices when a+b=2,3,4 and disjoint sets when a+b>=5 (all larger instances contain one of the a+b=5 configurations, up to swapping A,B and x0,x2). The C7 example has two minimum paired-dominating four-sets; one proposed exchange misses a vertex, the other leaves an unmatched vertex. Independent match-edge-pair and role-product enumeration plus BFS (`python3 /workspace/replay/audit_checks.py 4`, output `/workspace/replay/4.txt`) confirms counts and role equivalence on 36 small blowups, with complete distances and diameters when a+b<=8. Editorial caveats: the assumptions correctly require a perfect matching within G[S], not an induced matching, despite loose wording in the Finding and verification prose. The packaged C++ tests ordered ordinary basis exchange, not simultaneous symmetric exchange as its terminal label may suggest. Neither caveat affects the mathematical claim audited.

## originality

PASS

The established extremal family and scalar paired-domination number are background. The supported distinct contribution is the graph-specific rank-four transversal presentation of all minima, including the exact count and diameter. Classical distance and greedy conclusions are credited as standard once that representation is proved.

## value

PASS

The graph family is distinguished by a published edge-extremal paired-domination problem. Giving all optimum configurations by one four-role presentation yields exact optimizer counts, shortest relocation paths and minimum-cost placement for arbitrary vertex weights throughout the family. The C7 obstruction explains why the useful matroid property is not a general paired-domination theorem. The known extremal scalar and the generic matroid consequences alone would not provide this value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
