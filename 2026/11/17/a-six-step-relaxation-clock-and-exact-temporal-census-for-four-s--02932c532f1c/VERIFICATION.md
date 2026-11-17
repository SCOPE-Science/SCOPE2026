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

# Verification
The provided `verify_quotient.py` derives the exact cap-two map, tests all 59,049 signatures, and computes the weighted coefficient census for five graph orders. The independent C++17 `verify_direct.cpp` generates all full vertex states through six matched pairs and computes functional-graph distances without using the quotient. Both implementations were executed; their recorded text files are included and agree on their displayed counts. The complete finite quotient, not bounded direct simulations, establishes the all-size theorem. Re-run with `python3 verify_quotient.py` and `g++ -std=c++17 -O2 verify_direct.cpp -o check && ./check` (the latter prints to standard error).

The proof's essential checks are the single-excited-mate exception, saturation correctness, full-rotation safety condition, class entry bound, and multiplication by two for orientations of mixed-color matched pairs. The certificate does not assert an external independent audit or generalize to other graph families. All formulas concern deterministic labelled states.
