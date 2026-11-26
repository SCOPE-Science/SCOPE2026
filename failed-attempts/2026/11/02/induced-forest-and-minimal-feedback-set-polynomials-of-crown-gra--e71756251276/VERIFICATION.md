---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For shore sizes a,b and intersection c, the edge count ab−c exceeds a+b−1 for a,b≥3 or a=2,b≥4 and its transpose. The remaining cyclic exceptions are exactly disjoint 2-by-2 index sets and 2-by-3 sets with intersection smaller than two. Full containment in 2-by-3 gives a path; a nonempty overlap in 2-by-2 gives a path or a matching and permits extension to 2-by-3. Empty or singleton shores extend to (1,n), which is maximal precisely for n≥4; any acyclic 2-by-3 set is maximal. Counting these cases gives both polynomials, including M_3=6z^5 and M_4=32z^5. Complementation reverses inclusion and transforms sizes k to 2n−k, including 32z^3 at n=4. Simultaneous index permutations and shore interchange act transitively; two same-shore vertices have a common neighbor and the graph is regular and connected. Independent degree-at-most-one peeling of every vertex subset for n=3,…,7 reproduced the polynomials; the classification proves all n. Replay: python3 /workspace/branches/independent_finite_checks.py 1.

## originality

FAIL

An earlier distinct Resultary finding states the stronger shore-graded enumerators, the same maximal-set classification, the identical minimal-feedback polynomial and the identical support gap. A second earlier finding covers the all-forest enumerator with a component refinement on a larger graph family. This is demonstrable coverage in the indexed record, not a claim about worldwide priority.

## value

FAIL

An unbounded gap in inclusion-maximal forest sizes in a vertex-transitive bipartite family is a meaningful structural phenomenon, but it and the complete classifications are already supplied by the October 18 record. The remaining one-variable specialization and routine complement enumeration do not furnish independent mathematical value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
