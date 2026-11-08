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

# Reproduction and limits

Extract the two source files `verification/exhaustive.cpp` and `verification/symmetry.py`, retaining these relative names. Execute:
```
g++ -O3 -std=c++17 verification/exhaustive.cpp -o exhaustive
./exhaustive
python3 verification/symmetry.py
```
The C++17 standard-library program recursively enumerates all proper named four-colourings of the specified Grötzsch graph, constructs every legal one-vertex recolouring, performs a breadth-first search from **all 12,480 vertices**, and prints the components, degrees, eccentricities and every unordered pair count. Its last lines contain `components 2 6240 6240` and `ecc 15:2160 16:10200 17:120`. A sorted sixteen-plus-one position distance histogram is printed. The Python standard-library program independently enumerates via pentagon assignments, apex and shadow choice sets, constructs edges, checks reversibility, finds connected components, builds the full \(S_4\times D_5\) action and all 56 orbits, and searches from their representatives. It asserts the complete 17-entry pair-distance table, counts the 120 peripheral colourings and their unique antipodes, and replays the named 17-move witness. Successful completion prints `PYTHON_INDEPENDENT_PASS`.

Both source files were run successfully and their outputs were compared. The graph is finite and labelled, and all claims are strictly about it; this is not an infinite-case proof or a claim about arbitrary graph reconfiguration. Code does not establish historical originality or independent external audit. Independent audit has not yet been performed.
