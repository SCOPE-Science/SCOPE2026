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

In a directory containing `corner_morse.cpp` and `verify.py`, run `python3 verify.py` with Python 3 and a C++17 `g++` compiler available. The program builds from the accompanying source and enumerates every allowed simplex in dimensions 2–5. Each output boundary is constructed from signed augmented simplicial chains via elementary Morse-pair substitution, then checked for zero consecutive products and integral Smith invariants using actual unimodular unit pivots and zero residual matrices. Expected reduced homology groups are asserted; success prints `CUBE_THREE_CORNER_INTEGRAL_HOMOLOGY_OK`.

For the five-cube 3,302,633 simplicial faces are enumerated and exact Morse differential sizes include 757 by 73 and 16 by 757 (with orientation by matrix convention). The largest claimed free rank, 681, follows from exact critical counts and integral matrix ranks. This finite executable certificate does not prove a general statement for larger cubes. No independent external audit has been performed.
