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

# Verification procedure

Use the two source files embedded alongside this document. Run `python3 check_ring.py` with a standard Python 3 interpreter. Separately compile `check_coordinates.cpp` with `g++ -std=c++17 -O2 check_coordinates.cpp -o check_coordinates` and run `./check_coordinates`. Compare the stdout with `check_ring.out` and `check_coordinates.out`. The C++ program constructs the graph from Euclidean coordinates instead of sharing the Python cyclic edge list.

Both checkers enumerate the full finite solution space. The first tests all 30 potential first edges against every disjoint second edge, verifies that every successful pair uses an antipodal pair, and checks that the explicit antipodal construction matches all minimum four-sets. Both checkers independently construct the two single-replacement graphs and compute all-pairs shortest paths by breadth-first search from each of 135 states. Expected results: 135 minima; types 60/60/15; slide 360 edges, one component, radius and diameter six; jump 720 edges, one component, radius and diameter four.

Scientific scope: computations certify facts only for the explicitly defined twelve-vertex host. No finite experiment is used to justify an infinite extension. This work has received self-review but has not received independent audit or independent scholarly certification.
