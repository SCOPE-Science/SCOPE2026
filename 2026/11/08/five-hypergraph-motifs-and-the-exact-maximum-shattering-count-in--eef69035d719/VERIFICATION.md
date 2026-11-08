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

The finite-type reduction in RESULT.md converts all ordered four-supports into fifteen nonnegative incidence-cell counts satisfying four degree-three constraints. Thus the exhaustive search has a mathematically complete finite universe of cases for every ambient parameter. Run `python3 verify.py`: the program checks exactly 862 feasible membership vectors, determines all 40 shattering vectors and their five isomorphism orbits, and verifies exact rational coefficients plus the polynomial values for ambient sizes 3 through 18.

For an implementation-independent comparison, compile `direct_check.cpp` with a C++17 compiler and execute it. The direct graph-and-trace enumerator checks all candidate four-subsets for each ambient size 4 through 9 and compares its outputs with the predicted six counts. It does not use the incidence-cell classification.

Finite experiment alone cannot imply the all-parameter result; the proof relies on the complete fifteen-cell encoding and the fact that a center uses at most three coordinates outside the support union. The published Johnson-graph VC bound four is used only to identify size four as a maximum. The present package does not contain an independent audit of mathematical correctness, historical priority, or author provenance.
