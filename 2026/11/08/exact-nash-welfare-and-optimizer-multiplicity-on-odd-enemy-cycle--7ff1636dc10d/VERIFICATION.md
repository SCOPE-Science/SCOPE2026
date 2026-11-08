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

# Verification of odd-cycle Nash welfare

The complete proof is in `RESULT.md`. The attached C++ program `verify_cycle_nash.cpp` independently enumerates every unlabeled independent-set coalition partition of the enemy cycles with \(3\) through \(13\) vertices. It computes exact integer Nash products and optimizer counts; the odd-cycle outputs agree with the closed formula. Even orders serve as controls only. The independent Python program `verify_cycle_nash.py` uses a separate list-of-groups representation for sizes \(3\) through \(11\).

Run:

```bash
g++ -std=c++17 -O2 -Wall -Wextra verify_cycle_nash.cpp -o verify
./verify
python3 verify_cycle_nash.py
```

Expected terminal markers: `EXACT_ENUMERATION_OK` and `INDEPENDENT_EXACT_CHECK_OK`. For \(C_7,C_9,C_{11},C_{13}\), the C++ verifier reports Nash products \(8,648,82944,16000000\) and optimizer counts \(14,54,88,130\). This enumeration checks only finite orders. The analytic proof establishes the stated result for every odd cycle.
