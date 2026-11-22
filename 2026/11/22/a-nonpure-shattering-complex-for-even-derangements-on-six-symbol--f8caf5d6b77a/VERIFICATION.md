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

# Reproducibility

The executable certificate consists of `verify_python.py` and `verify_cpp.cpp`. The first enumerates even derangements by inversion parity and nonattacking partial assignments by chosen row/column sets. It computes face counts, identifies maximal faces, checks all their simultaneous-label-permutation orbits and performs binary boundary elimination. The second enumerates hypotheses by cycle parity, potential faces by recursive cell insertion and independently performs trace testing and GF(2) boundary elimination. All steps use finite integer operations.

Run `python3 verify_python.py`, then `g++ -O2 -std=c++17 -o verify_cpp verify_cpp.cpp` and `./verify_cpp`. The scripts assert the 130-concept count, the full face sequence, facet counts, and ranks \((1,29,286,750)\). The Python verifier additionally lists and verifies the facet-orbit decomposition. Computations were replayed from the extracted submitted source files before release.

The exact finite calculation does not prove an all-order or integral-homology statement. No independent external mathematical audit has been performed.
