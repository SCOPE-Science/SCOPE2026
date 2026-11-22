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

# Reproduction

From the same directory, run `python3 verify_nauru_py.py` and compile/run the C++17 verifier using `c++ -O2 -std=c++17 verify_nauru_cpp.cpp -o verify_nauru_cpp && ./verify_nauru_cpp`. Each checker constructs the twenty-four-vertex graph from the three edge families, enumerates all 346,104 seven-vertex subsets and compares its results to fixed integer assertions or printed exact counts. The Python method directly simulates infection; the C++ method first checks induced-forest components and edges, then simulates infection. Both computations were executed successfully and returned 12,384 successes with completion-time counts (120, 3288, 6456, 1584, 936) and matching component-type cells.

The Python checker also checks all 120 fastest residual forests and all 936 slowest residual forests, confirming the asserted order/diameter counts. Finite exhaustive computation is a certificate only for the stated finite graph. Self-review only; independent audit not performed.
