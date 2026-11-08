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

The source files are complete and standalone. Python 3 and a C++17 compiler are sufficient. Run `python3 verify_transfer.py`, then `g++ -std=c++17 -O2 verify_vertex_constraints.cpp -o check` and `./check`.

The Python program enumerates row transitions with four-bit words; the C++ program propagates degree-two constraints over thirty-two individual edge bits. Each enumerates the entire state space, generates legal directed elementary-face reversals, checks flux conservation, and performs complete breadth-first shortest-path calculations. The Python program checks the explicit twelve-face witness and the two central metric centers. Assertions compare actual results to the scientific statement; no stored graph data or external datasets are read.

The finite proof is exhaustive for the labelled \(4\times4\) torus only. An arithmetic height-potential lower bound supplies a separately checkable certificate for one distance-twelve pair. The finite computational search does not assert anything about larger toroidal grids or other transformations. Independent scholarly validation is not represented here.
