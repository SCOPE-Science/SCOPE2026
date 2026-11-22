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

The two embedded standalone programs have different distance constructions: `verify_bfs.py` builds the disjointness graph and computes breadth-first-search distances; `verify_intersection.cpp` uses the explicit intersection-class distance law. For each labelled graph with \(7\le n\le11\), both examine every unordered vertex pair, every potential landmark, and every resulting exact bisector. Their outputs establish the same finite minimum resolving-neighborhood size, threshold and distinct maximum-bisector multiplicities.

The Python and C++ output records are attached as `verify_bfs.out` and `verify_intersection.out`. Re-run with `python3 verify_bfs.py`, then `c++ -O2 -std=c++17 verify_intersection.cpp -o verify_intersection && ./verify_intersection`. Required dependencies are the Python standard library and a C++17 compiler. No binary dependency, external data, or network access is required.

Computational verification covers only \(7\le n\le11\). For all \(n\ge7\), correctness rests on the independently stated combinatorial distance-count and incidence-frequency proof. The check does not perform an external audit, establish originality, or settle unmentioned parameters.
