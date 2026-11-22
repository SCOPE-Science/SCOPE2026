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

## Reproduction

The full census is computed by `rank3_burnside.cpp` without third-party libraries. Compile with `g++ -O3 -std=c++17 rank3_burnside.cpp -o rank3_burnside`, then execute `./rank3_burnside`. Its 15 cycle-type loops check all fixed graphs, and it verifies the 10 nonzero edge-count coefficients independently of any supplied output file. The exact produced table is in `CENSUS_OUTPUT.txt`.

Run `python3 rank3_recursive.py` with the included `atlas_le7.g6` in the same directory. This second implementation evaluates the original game recursion over all 1,253 unlabelled graph-atlas representatives through seven vertices. It independently confirms 372 qualifying seven-vertex types, the edge coefficient distribution, and absence below seven vertices.

The rank-to-root characterization and the Burnside summation are proved in `RESULT.md`. The finite program is exhaustive only for the stated seven-vertex edge space. The graph6 atlas data are a separately generated comparison input; the complete Burnside calculation does not rely on them. No independent audit or external certificate has been performed.
