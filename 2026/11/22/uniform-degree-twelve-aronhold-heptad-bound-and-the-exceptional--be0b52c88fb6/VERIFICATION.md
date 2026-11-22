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

With a C++17 compiler, compile and execute `verify_aronhold.cpp` using `c++ -O2 -std=c++17 verify_aronhold.cpp -o verify_aronhold && ./verify_aronhold`. The verifier constructs all theta refinements, 288 Aronhold heptads, 1,451,520 symplectic matrices, 30 pairwise distinct theta-cycle signature classes and all heptad permutations for one representative of each signature. The text files `minimum_degrees.csv` and `class_profiles.csv` contain the exact evaluated summaries, not substitutes for the executable proof.

The supplied program has been executed. Its stderr reported `aronhold=288` and `reps=30`; its stdout ended with the eight minimum-degree lines reproduced in `minimum_degrees.csv`. All 30 class sizes sum to 1,451,520. One representative has size-120960 class, odd minimum 1, even minimum 6, and 24 Aronhold cycles of length 12.

The completeness argument depends on the independently tabulated fact that the symplectic group has precisely 30 conjugacy classes; 30 distinct invariant paired signatures thus label them without identifying group matrices via conjugation. Geometric realizability of all abstract Frobenius classes has not been checked and is not claimed. This is not an independent audit.
