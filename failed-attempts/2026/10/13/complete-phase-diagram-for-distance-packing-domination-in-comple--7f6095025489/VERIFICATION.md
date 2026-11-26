---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For nonempty parts and r≥2 the two distinct-vertex distances are 1 across parts and 2 within each part (only 1 occurs when all parts are singletons). Thus p=0 leaves all sets, p=1 permits only sets in one part, and p≥2 restricts to at most one vertex. Independently d=0 requires V, d=1 permits exactly the sets meeting multiple parts or equal to a whole part, and d≥2 permits all nonempty sets. The generating function for sets meeting multiple parts is (1+x)^N−1−Σ_i((1+x)^{n_i}−1), disjoint from the whole-part contributions. Intersecting with the three packing filters gives all eight cases; the empty set is never feasible and V is invalid for d=0,p≥1 because an across-part pair exists. The smallest nonzero exponents match the second table, including no universal vertex when q=0 and all the infinite cases. A separate BFS and subset replay (python /workspace/branches/independent_reproduction.py 2) matched all cardinality coefficients on seven profiles, including cliques, singleton parts and profiles with none, for all 36 parameter pairs 0≤d,p≤5; the general result follows from the distance argument. The frozen verifier and recorded output were inspected, not executed.

## originality

FAIL

The combined table was not found verbatim. But its main counting cell, the full ordinary domination polynomial for arbitrary complete multipartite graphs, is already Theorem 2(ii) of Alikhani–Torabi. The combined table is that known polynomial and its immediate consequences or filters from the published definitions on a metric of diameter at most two, rather than a distinct exact counting result beyond them.

## value

FAIL

The table is a convenient summary, but its apparent extra scope is entirely an immediate diameter-two case split. Once the known ordinary domination polynomial is credited, no unknown exact invariant, nonobvious boundary, or stronger structural lemma survives. The two remaining packing filters amount to taking whole classes or singletons, or counting all their subsets when domination becomes automatic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
