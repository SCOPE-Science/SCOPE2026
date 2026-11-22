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

The graph is the explicit generalized Petersen graph with sixteen vertices and twenty-four edges. The complete exhaustive domain consists of every one of its \(65536\) vertex masks.

`check_cpp.cpp` uses shortest-path breadth-first search and precomputed distance-separating masks. `check_python.py` independently uses all-pairs shortest-path distances and complete distance-code comparisons, then enumerates all host-graph automorphisms and computes all shortest paths of the optimum exchange graph. Both were executed successfully with their assertions enabled.

The key exact test for a pair of vertices \(a,b\) is at least one selected distance separator; when exactly one endpoint is selected, two selected distance separators are necessary and sufficient. This checks *resolving* weak-total sets rather than the weaker *pure* condition that omits resolution among unselected vertices.

The verification is exhaustive for this finite graph, not a certificate for an infinite graph family. It is reproducible with Python 3 and NetworkX 3 or a C++17 compiler. No independent scholarly validation is claimed.
