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

# Verification of the finite Schur-equation sensitivity theorem

The reproducibility package contains `critical_triples.csv`, `verify_direct.py`, `verify_incremental.cpp` and `verify_rigidity.py`, all independently executable with standard Python 3 and a C++17 compiler. The two primary methods independently compute the same 49-vector of deletion multiplicities, not merely a preprinted summary.

1. Run `python3 verify_direct.py` alongside the CSV. It directly evaluates each of the 49 equations over all 3^13 normalized colorings and checks every count; it confirms zero defect-free, 1350 single-defect normalized, 4050 single-defect named and 29 critical equations.
2. Compile `verify_incremental.cpp` with `g++ -std=c++17 -O2 -o verify_incremental verify_incremental.cpp` and execute `./verify_incremental`. Its branch-by-branch incremental assignment independently checks every CSV entry, with a safe prune at the second violation.
3. Run `python3 verify_rigidity.py`. It checks the six normalized valid [1,13] colorings, their three fixed blocks with position seven free, and at least two monochromatic sum-14 equations for each possible endpoint color.

Both primary implementations have been executed successfully on the supplied files; source scripts and CSV enable repetition, not an independent scholarly audit. The proofs use a complete finite search only at n=14. Unindexed published exact tables could affect historical originality, and no claim of independently certified priority is made.
