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

For a selected set with shore sizes a,b and c selected matched pairs, the total shortest-path length budget is k(k-1)-ab+2c, k=a+b. It is less than n(n-1) for k<n, and also for mixed k=n when n≥5 since ab>2c. A full shore at even n would need n/2 endpoint pairs at each omitted vertex, more than the total number of shore pairs. At odd n, on indices modulo n, assigning {i,j} to omitted index (i+j)/2 constructs the near-one-factorization and covers everything. For k=n+1, a mixed set with a,b≥2 omits c-1 matching pairs and leaves (a-1)(b-1)-(c-1) edges with both endpoints omitted. Each can only be the middle edge on a geodesic of a selected matched pair. Thus (a-1)(b-1)+1≤2c≤2min(a,b), impossible for a+b≥7 and a,b≥2. Finally for even n the chosen full shore plus b_0 works: the near-one-factorization on the odd index set excluding 0 covers the remaining neighbors of each b_t except a_0; one deranged assignment of pairs {a_0,a_j} supplies those omitted edges without duplicating a pair or using a forbidden edge. Edges at b_0 use direct paths. This proves both minima and the claimed complete optimizer families in scope; choosing additional unused pairs if required cannot spoil coverage.

## originality

PASS

The complete bipartite baseline and its optimum-set structure are known. The distinct theorem covers the graph after deleting a perfect matching, with new length-three paths and an odd-order drop of two in the minimum. The checked crown literature studies different coverage conventions. Bounded literature and index comparisons support the distinct crown strong-edge theorem without establishing historical priority.

## value

PASS

Crown graphs are the standard one-perfect-matching deletion from the balanced complete bipartite family. The exact minimum detects a parity-sensitive effect of that deletion, while complete rigidity answers the more restrictive question of which endpoints an optimal cover can use. The number of eligible matching pairs controls the new length-three capacity; this explains why extra shortest paths do not produce mixed-shore minimizers once n≥5. This is a structural result rather than a recomputation of the complete bipartite minimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
