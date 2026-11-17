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

# Reproduction of the two-cluster ultrametric Euclidean inball theorem

Run `python3 verify_two_cluster.py` in the same directory as this document. Only the Python standard library is needed. The program constructs the metric on labeled clusters, solves signed tight differences along every labeled spanning tree for each selected metric of at most six points, rejects all potentials violating Lipschitz constraints using exact fractions, and deduplicates the resulting polar vertices. It constructs the predicted two-level potential set separately, checks equality of these sets, computes every centered squared norm, counts all maximum-norm vertices, and performs exact rational Gaussian elimination on the contacting normals.

The seven selected cases are \((p,q,s,t)=(2,2,2/5,3/4),(2,3,1/3,9/10),(2,4,3/5,2/3),(2,4,9/10,4/5),(2,4,1/6,9/10),(3,3,4/7,5/6),(2,4,4/5,4/5)\). The fourth case is exactly at the first contact transition, and the fifth lies strictly above it. The program additionally exhausts all count pairs for \(2\le p\le7\), \(p\le q\le21\), and sixteen independent rational pairs of the within-cluster distances, checking that no maximizing potential has a positive smaller-cluster count.

Expected successful final line:

```text
ALL_TWO_CLUSTER_SCREENING_AND_PHASE_CHECKS_PASS
```

The printed preceding lines list the small exact polar-vertex counts, tangent counts, and contact ranks, so they can be matched directly with the formulas. These finite tests do not prove the theorem for all integer cardinalities and arbitrary real lengths. The proof of the strict screening exchange, concave integer optimization, and full affine center dimension is analytical and appears in `RESULT.md`.
