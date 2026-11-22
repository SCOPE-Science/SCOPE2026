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

The included `verify_orbits.py` uses the Python standard library. It builds the affine hyperedges as three-point arithmetic progressions, checks all 19,683 three-color assignments, enumerates every affine transformation and colour renaming, tests the five complete symmetry orbits and runs breadth-first searches from their representatives. It also computes the full chromatic polynomial by all 4,096 subsets of the twelve line constraints. Running it reproduced 3,762 proper colourings, five orbits, 16,848 edges, radius nine, diameter ten, and 306 unordered diameter pairs.

The separately implemented `verify_all_pairs.cpp` uses a different construction of the twelve lines, via their four linear directions. Compile with `g++ -std=c++17 -O2 verify_all_pairs.cpp -o verify_all_pairs` and run the executable. It enumerates all 3,762 valid labelled states and performs one BFS from each state, independently reproducing the complete distance and eccentricity histograms recorded in `all_pairs.out`. Each traversal checks that all valid states were reached.

## Exact scope and failure modes

The two programs use exact integer arithmetic. The chromatic identity holds for all positive palette sizes by finite inclusion-exclusion, but the reconfiguration result applies to a **three-colour** palette and single-point recolouring. Exhaustion of this finite hypergraph does not prove comparable statements for larger geometries. Matching two computations is corroboration, not independent expert audit or global priority certification.
