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

# Reproducibility of the mathematical checks

`recurrence_check.py` enumerates the nine pairs of child-attachment colors and derives coefficient arrays `(5,6,2)` and `(4,4,1)` by polynomial multiplication, independently of any written table. It checks the exact integer recurrence at heights zero through six and evaluates the entropy series as a numerical sanity check.

`direct_check.cpp` constructs the finite triangular block trees and implements the original synchronous three-state Greenberg–Hastings rule, including the excitation condition for a resting vertex. It directly checks first-return-at-three without equating successor support to period three. All 27 states for height zero, 2,187 for height one, and 14,348,907 for height two were visited. Observed primitive-three counts are 6, 102, and 36,390. The outputs in `recurrence_check.out` and `direct_check.out` were captured by running these exact programs.

Reproduce using `python3 recurrence_check.py` and `g++ -std=c++17 -O3 direct_check.cpp -o direct_check && ./direct_check` (a local C++17 compiler is necessary). Runtime depends on hardware. The all-height statement is proved by the finite case split in the accompanying mathematical result, not by an extrapolation from these tests. This document does not report independent or external verification.
