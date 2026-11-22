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

# Reproducible finite verification

Use `python3 verify_exact.py` and `c++ -std=c++17 -O2 verify_independent.cpp -o verify_independent && ./verify_independent`. Match stdout to `verify_exact_output.txt` and `verify_independent_output.txt` respectively. Both methods enumerate every 13-bit nonempty subset and every size-four minimum exchange edge; shortest-path metrics are obtained from all 260 sources. The Python adjacency uses explicit residues and flood fill, whereas the C++ adjacency uses Euler's quadratic-residue test and union-find. No randomized sampling, external solver, downloadable data table, or stale certificate is necessary. A finite exhaustive algorithm verifies this specific finite graph, not any other graph order. Independent scholarly validation has not been performed.
