---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Petersen vertices are 2-subsets of five labels, distance 1 iff disjoint and 2 iff intersecting and distinct. Within-block nonseparation is equivalent to all other blocks having the same neighbor-incidence bit; different blocks separate via coordinate zero. Restricted growth words uniquely enumerate all unlabeled partitions into k blocks. Independent from-scratch C++ enumeration at k=2,3,4 gave 0,0,7040 valid. For each of the 7040 canonical k4 states, checked all single-element moves to another nonempty class, yielding 34500 unordered edges. BFS from ALL 7040 vertices yielded eccentricity 7 for 6300 and 8 for 740, and 24777280 unordered distance pairs; connected, radius7 diameter8. Exhaustion of finite 10-vertex graph makes exact finite proof, not a sample or inference for larger graphs.

## originality

PASS

Existing published general partition-dimension literature supplies scalar pd(P)=4 and bounds for generalized Petersen graphs, but not the state-by-state optimum partition family, single-vertex transfer graph, its complete edge count and exact diameter. Resultary search found no exact covering theorem besides the same November 8 finding; best of knowledge, subject to inaccessible older literature.

## value

PASS

The connectivity and sharp transfer distances of all optimal resolving sensor/block placements are a natural reconfiguration problem independent of the scalar partition dimension. 7040 exact states, degrees, orbit shapes and diameter answer concrete structural questions, not a tiny arbitrary slice. A bounded Petersen graph is a canonical natural object for which the exact complete state space is a useful benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
