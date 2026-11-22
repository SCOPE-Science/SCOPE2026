---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For 12 vertices the domain is precisely all 4096 bit patterns on each of the 25 graphs; there are no hidden parameters. The source lists all 24 undirected edges and the integer majority/tie map. I rebuilt an entirely separate 4096-state map and path-to-cycle census for all 24 deletions plus the original: baseline (234 fixed,136 two-cycles,max depth7,32 maximizing,basin2906); class representatives (0,1),(0,6),(2,3),(2,6),(2,8) have (118,82,11,24,3164),(130,106,8,2,3094),(126,118,7,20,3032),(106,78,7,8,2996),(144,128,8,4,3080), respectively. All possible least periods were 1 or 2. The source separately enumerates the graph automorphism edge orbits of sizes (4,8,4,4,4), so positivity of all five basin differences proves universal all-edge claim. The finite domain is exhaustively enumerated, not sampled.

## originality

PASS

The Goles–Olivos threshold-cycle theorem supplies only period≤2, and Chvatal graph classical work supplies the graph. Other published majority-edge perturbation classifications are on Heawood, Robertson, Frucht, and complete bipartite graphs, not this graph/rule and 25-map census. The Chvatal Tutte polynomial is unrelated. Unindexed prior machine census remains a risk.

## value

PASS

A famous smallest regular triangle-free four-chromatic graph is a natural finite stress test of majority dynamics; the every-edge consensus gain with an enlarged worst transient is a nontrivial exact graph-specific robustness phenomenon and the complete basin census is reusable, notwithstanding no global monotonicity theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
