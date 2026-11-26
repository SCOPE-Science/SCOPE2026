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

The eight token types give two branch blocks that are incidence graphs of K_a and K_b, and a mixed block with left shore L consisting of opposite-center/leaf pairs and right shore consisting of mixed-leaf pairs and the double-center pair XY. Within a branch of size t, the minimum cover and maximum matching are min(t, binom(t,2)); for t≥3 the cyclic successor edges match the t leaf-vertices. Omitting p leaf-vertices forces p(2t−p−1)/2 edge-vertices, so t≥4 makes every p>0 strictly worse; t=3 ties only at p=3, and t=1,2 give the unique empty or sole edge-vertex cover. For a,b≥2 one can match L into mixed-leaf pairs alone: these are incidence edges of K_(a,b), which has a spanning unicyclic subgraph, so assign vertices one outgoing edge by orienting the cycle and directing off-cycle paths toward it. When a=1, match the b opposite-center pairs on the b side to their distinct mixed-leaf neighbors and the remaining vertex to XY, or symmetrically. Combining block matchings and the covers with L proves the exact scalar formulas. In every global minimum cover the restriction to each block is minimum. Omitting any L-vertices when a,b≥2 forces at least that many distinct mixed-leaf vertices plus the extra XY. For a singleton branch, its empty incidence cover forces the corresponding L-vertex via the interblock edge; omitting any other L-vertex then likewise forces its distinct mixed-leaf match and XY. The mixed block by itself need not have a unique cover at this boundary, which is why the interblock edge is essential. All remaining choices are independent because interblock edges meet L. Taking complements yields the claimed mandatory configurations, branch-size-three choices and exact number of maxima. Fresh exact optimizer and matching checks corroborated all nine pairs 1≤a,b≤3, and (4,1) with 21 vertices, alpha 12, matching/cover 9 and one maximum independent set.

## originality

PASS

Pass the distinct general double-star matching/cover result and complete optimizer classification, including the independent size-three tie. Scalar boundary cases are covered by prior bounds and parity, and same-host domination and different complete-bipartite-host classifications are substantial but not equivalent. The matching/cover/independence identities themselves are standard and not claimed as separate advances.

## value

PASS

Double stars are a natural sparse tree family just beyond stars and paths; their large instances fall outside the principal perfect/near-perfect-host matching guarantee. The exact matching/cover value and the full set of maximum configurations reveal when either branch contributes a genuine degeneracy. The size-three threshold and independent choices supply optimizer information unavailable from a numerical scalar or from domination.

The dated certificate retains the supplied scientific assessment, sources and limitations.
