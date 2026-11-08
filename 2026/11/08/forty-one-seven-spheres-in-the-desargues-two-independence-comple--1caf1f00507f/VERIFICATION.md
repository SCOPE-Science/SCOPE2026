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
# Verification of the Desargues two-independence calculation

Compile the included standalone `verify_desargues.cpp` using a C++17 compiler, for example `g++ -O2 -std=c++17 -Wall -Wextra -pedantic verify_desargues.cpp -o verify_desargues`, then run `./verify_desargues`.

The checker verifies the graph's two different constructions by a twenty-entry permutation that preserves all adjacency relations. It computes the \(P_3\)-free faces independently by induced-degree recurrence and by excluding every three-vertex path of the incidence-graph realization, comparing all masks. It counts faces, maximal faces and the Euler characteristic. It builds the two stated matchings, checks pair uniqueness and dimensions, and explicitly constructs indegrees of the complete reoriented face-poset covering graph. A complete topological ordering, for *each* matching order, verifies acyclicity. The logged output is contained in `verification_output.txt`; this output alone is not evidence without rerunning or reviewing the checker.

Checks reproduced: graph orders \(20\) and sizes \(30\); \(62{,}048\) nonempty faces; \(31{,}003\) pairs; one critical vertex; forty-one critical dimension-seven faces; \(400{,}760\) incidences; and a complete \(62{,}048\)-vertex topological sort. No computation relies on probabilistic sampling. The check is finite and graph-specific; it does not verify a larger family or independent priority.
