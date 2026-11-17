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

# Exact finite verification

The state space is explicitly all 4096 binary assignments to the twelve edges of a 3-cube. `verify_cuboctahedron.py` computes the graph from the cube edge incidences, evaluates the synchronous majority map at every state, tests every second iterate, classifies all entrance depths and attraction basins, and calculates the 48-element symmetry action and orbit representatives. `verify_cuboctahedron_independent.cpp` uses an independently written twelve-mask array and bit-popcount rule, first verifies that array against edge incidences, then checks the same complete transition and basin census.

The captured output files correspond to the supplied source programs and contain the exact counts. Reproduce with `python3 verify_cuboctahedron.py`, `g++ -O2 -std=c++17 verify_cuboctahedron_independent.cpp -o check`, and `./check`. State integer `348` attains the maximum first-entry time four. All 40 phase states of primitive two-cycles have transition indegree one. The Python verifier gives 14 fixed geometric classes and three two-cycle geometric classes of sizes 8, 6 and 6. There is no Monte Carlo sampling, convergence extrapolation, or claim for all four-regular graphs.
