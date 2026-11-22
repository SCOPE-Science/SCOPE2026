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

# Reproduction record

Execute `python VERIFY.py` (Python 3.10 or later, SymPy), and compare its terminal output with `VERIFY_output.txt`. The script generates all multihomomorphisms from the labeled five-cycle into the six-point two-subset Kneser graph, calculates all codimension-one CW incidences, exhaustively removes unique-coface pairs, constructs signed two-cell boundaries, contracts a spanning tree, and performs integral unit-pivot reduction followed by exact SymPy Smith form on its seven-row residual.

Verified cell count 104220 in dimensions zero through five; 32058 valid CW free-face pairs; remaining CW cells 6570, 19692 and 13842 in dimensions 0, 1 and 2. One connected component. Independent mod-two boundary rank 13113. Integral boundary rank 13114 with 13113 unit invariant factors and exactly one invariant factor 2. These imply first homology free rank 9 with one 2-torsion class and second homology free rank 728. The 0, 1, 2-dimensional ranks and absent higher-dimensional cells after collapse are explicitly checked by script assertions.

The finite computation is exhaustive for the specified finite complex. It is not an infinite-family proof or evidence of an independently verified mathematical audit.
