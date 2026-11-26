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

The duad–syntheme incidence construction gives the specified simple cubic bipartite graph. Two disjoint duads share a unique syntheme, precluding a 4-cycle; three pairwise disjoint duads exhaust the base set and force the same syntheme, precluding a 6-cycle. The independent replay exhausts the perfect matchings by branching on the least uncovered vertex. It builds transitions both by enumerating all simple 8-cycles and by testing every matching pair for a connected eight-edge difference. The edge sets agree: 90 cycles, 32 alternating matching endpoints per cycle, 288 matchings and 1440 flip edges, all vertices of degree 10. Complement traversal gives exactly 144 of each stated type and every edge crosses the two types. All-source BFS covers all 288 vertices and yields (1,10,42,97,101,37,0) for type (30) and (1,10,45,97,96,37,2) for type (10,20), proving the radius, diameter and center. Exact comparison with the frozen JSON certificate agrees for the incidence edges, cycles, states, types, transitions and all distance histograms.

## originality

FAIL

A distinct Resultary record, 2d0e450ce331, gives exact equivalent coverage of the intrinsic exchange graph and both type-indexed metric rows, and further characterizes all antipodes. Its proof generates the exact labeled adjacency and complementary types, from which the absence of same-type edges is an immediate check. The substantive frozen result is covered in the reviewed catalogue. The matching record is catalogued under a later date; this audit does not claim it predates the frozen record or determine independent discovery or priority.

## value

FAIL

The intrinsic shortest-cycle reconfiguration metric of this cage is a worthwhile exact invariant. In this review, however, the same computed graph, full metric strata and a stronger antipodal invariant are already available in a distinct record; testing the type labels on the same edge list adds no substantial covered-gap remainder. This is not a rejection of finite graph computations as a class.

The dated certificate retains the supplied scientific assessment, sources and limitations.
