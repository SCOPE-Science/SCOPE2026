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

The two included verifiers are standalone. With a C++17 compiler, run `g++ -std=c++17 -O3 verify_bipartite_triangular.cpp -o verify` followed by `./verify`; with Python 3, run `python3 verify_bipartite_triangular_series.py`.

The C++ program constructs triangular-graph adjacency independently of the component characterization. It examines every subset of every triangular graph for base orders from two through seven, tests bipartiteness by breadth-first two-coloring, tests inclusion-maximality by every one-vertex extension, and compares cardinality coefficients against a separate base-component enumeration. Its successful output terminates with `VERIFY_OK graph_orders=2..7 candidate_subsets=2131018 bipartite_subsets=15470 maximal_subsets=3442 graph_level_and_base_structure=PASS`.

The Python program computes cycle-cover counts by the combinatorial recurrence for the cycle containing the least available label and compares induced maximal cardinality counts with the rational series from the theorem for all base orders from two through thirty. Its successful output ends with `VERIFY_OK exact_component_recurrence_and_series n=2..30 odd_well_bicovered=PASS even_two_sizes=PASS`.

The finite checks do not prove the general theorem or establish publication priority. No independent mathematical audit has been performed.
