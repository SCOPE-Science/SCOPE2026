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

# Reproduction and proof limits

Run `python3 verify_grid.py` and independently compile and run `verify_grid_factoradic.cpp` with a C++17 compiler. The Python program exhausts 362,880 nine-byte permutation states and twelve legal grid-edge swaps from each state. Its assertions cover the full distance-layer histogram, unique distance-16 configuration, and the all-state half-Manhattan lower-bound deficit histogram. The C++ source independently uses factorial ranking and the same graph definition, with assertions on the same counts.

The BFS correctness argument depends only on exhaustive vertex discovery, complete neighbor enumeration and FIFO layer order; the graph's 9! states are actually all visited. The theoretical Cayley vertex-transitivity and parity arguments turn the one-source census into exact all-source radius/diameter and antipodal-pair statements. The finite classification cannot imply results for larger meshes or for the blank-space sliding puzzle. No independent human or external audit is asserted.
