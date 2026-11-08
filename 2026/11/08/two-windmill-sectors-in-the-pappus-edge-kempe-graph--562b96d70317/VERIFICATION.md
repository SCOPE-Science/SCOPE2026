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

# Verification

On the exact companion files, execute:

```sh
python3 matching_checker.py
g++ -O2 -std=c++17 coloring_checker.cpp -o coloring_checker
./coloring_checker
```

The first program uses a recursive perfect-matching census followed by independent complementary-cycle alternation. It verifies 42 perfect matchings (36 with Hamiltonian complements, six with three hexagons), the six complete exceptional edge-index lists, the two triples of exceptional matchings, the 20 states and the graph isomorphism.

The second program uses direct edge-by-edge constrained three-coloring, canonical color normalization, alternating-cycle switching, component BFS and the induced triangle-clique checks. It independently verifies 20 unlabelled states, 36 adjacencies and two components, each the cone over three triangles. Both programs were actually executed successfully after compilation (where needed). All required dependencies are the Python 3 standard library and a C++17 compiler; no external computation logs or files are prerequisites.

This is exhaustive finite verification for an explicitly specified graph, not a proof of general statements about larger graphs. Only a self-review has been conducted; no external or independent audit is represented.
