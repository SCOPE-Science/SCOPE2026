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

# Reproduction and evidence limits

The accompanying self-contained files `verify_exhaustive.cpp` and `verify_orbits.py` use distinct generation and shortest-path reductions. In the same directory, run:

```sh
g++ -O3 -std=c++17 verify_exhaustive.cpp -o verify_exhaustive
./verify_exhaustive
python3 verify_orbits.py
```

`verify_exhaustive.cpp` checks all \(4^{10}\) assignments, constructs valid recolouring edges directly, checks adjacency symmetry and all-source breadth-first search distances. Expected four-colour output includes `states=12960`, `edges=53280`, `radius=13`, `diameter=14`, `13:3360`, `14:9600`, and `14:44400` in the pair-distance table. Three-colour output checks \(60\) disjoint edges.

`verify_orbits.py` independently backtracks through proper colourings, uses all \(120\) induced automorphisms from permutations of five underlying points, enumerates all \(540\) colour-canonical configurations, verifies the eleven symmetry orbit representatives and their shells, and checks the weighted pair-distance table, including \(44{,}400\) unordered pairs at distance \(14\). It also reconstructs the displayed fourteen-step witness sequence and checks each move and the endpoint distance.

These executions give an exhaustive finite verification for the stated ten-vertex graph. Neither script certifies scientific priority or generalizes the computation to infinitely many graphs. Independent scholarly auditing has not been performed.
