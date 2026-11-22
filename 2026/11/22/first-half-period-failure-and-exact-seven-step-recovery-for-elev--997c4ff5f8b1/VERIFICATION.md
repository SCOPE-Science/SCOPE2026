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

## Exact reproducibility checks
C++17 compilation and execution from the packaged source succeeded. `check_horizon.cpp` exhaustively generated 2, 24, 720 and 3,628,800 canonical cycles of lengths 3, 5, 7 and 11 respectively, finding the minimal observation horizons 1, 3, 4 and 7. It reproduced the six-step eleven-cycle histogram (fiber sizes 1: 3,470,400; 2: 77,760; 4: 720) and counted 82,080 ambiguous unordered pairs, then showed all seven-step keys distinct.

The independently written phase-index implementation `check_phase.cpp` reproduced the eleven-cycle six-step histogram and seven-step uniqueness. The direct third implementation `check_witness.py` verified the given two distinct cycles match for the first six observations and differ at the seventh. See `CHECK_OUTPUT.txt` for the exact recorded outputs. All comparisons are integer-valued and exact; no floating-point heuristics are used.

The finite domain was fully traversed, so the enumeration is an exact proof for the four specified lengths. The checks do not prove any statement for larger prime lengths, global interval maps, or robustness to incomplete/noisy ordinal observations. No independent mathematical audit was performed.
