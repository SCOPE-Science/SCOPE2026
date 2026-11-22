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

# Exact reproducibility

`census.cpp` is an exhaustive standalone C++17 graph enumerator. Compile with `g++ -O3 -std=c++17 -o census census.cpp`, then run `./census`. It iterates all \(2^{\binom n2}\) labelled simple graphs for each \(1\le n\le7\), tests all four-cliques, computes each graph's triangular vertex mask and alternating subset sum, and verifies that every coefficient outside \(\{-1,0,1\}\) is the value \(2\) for a six-rim wheel. Expected terminal line: `EXHAUSTIVE_CENSUS_OK`. Expected seven-vertex totals: \(1486597\) labelled four-clique-free graphs, of which \(420\) have the exceptional coefficient.

`verify_wheel.py` uses only the Python 3 standard library. It constructs the wheel's exact \(128\times128\) feasibility matrix and applies the integer Boolean Möbius transform to both axes. All off-diagonal entries must vanish; the diagonal has \(105\) zeros, \(22\) unit entries and one entry equal to \(2\). Expected terminal line: `WHEEL_VERIFY_OK`.

These are exact integer calculations, not floating point experiments or partial sampling. They prove only the finite sharp classification and the wheel's integer diagonal; the separately written general Möbius proof covers arbitrary finite bases at the structural level. Neither script attempts a historical literature audit or independent external validation.
