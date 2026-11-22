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

The complete finite icosahedron census uses two self-contained verification programs. Running `python3 -S verify_python.py` produces `ICOSAHEDRAL_MIXED_VERIFY_OK`, and compiling and running `verify_cpp.cpp` with a C++17 compiler produces `ICOSAHEDRAL_MIXED_WITNESS_VERIFY_OK`.

Both rebuild the graph, enumerate the entire \(2^{12}=4096\)-subset space, evaluate all 42 graph elements, check the exact all-size and inclusion-minimal coefficients, verify the antipodal-triple structure and ten-plus-ten induced geometries, and establish the connectivity threshold through all feasible states of sizes at most eight. The algorithms use different resolving tests (signature uniqueness and pairwise witness masks) and different shortest-path algorithms (BFS and Floyd–Warshall).

The result establishes no analogous theorem for other graph orders, generalized antipodal graphs, or other notions of distances to edges. The checks are finite and exhaustive only for the specified labelled graph. Independent external validation has not been performed.
