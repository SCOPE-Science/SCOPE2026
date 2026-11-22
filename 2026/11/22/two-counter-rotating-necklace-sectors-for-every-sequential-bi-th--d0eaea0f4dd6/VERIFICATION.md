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

The embedded C++ source `checks/check_all_orders.cpp` directly implements the in-place local update for every schedule on every cycle size from 3 through 8. It classifies periodic states from the full directed functional graph, checks the ascents-derived recurrent set, and compares all period-dividing-d counts for d up to n. Its saved output records all 46,230 schedules and 11,017,392 schedule-state pairs passing.

A separate Python implementation `checks/check_sampled.py` directly iterates the local threshold rule and checks the one-species sector property and that mixed species collide within a bounded number of sweeps: every permutation through n=6 and specified randomly seeded samples through n=10, with all binary configurations for each schedule. The output records 1,040 checked schedules.

To reproduce, use `g++ -O2 -std=c++17 checks/check_all_orders.cpp -o /tmp/cycle_scan_check && /tmp/cycle_scan_check` and `python3 checks/check_sampled.py`. No finite enumeration proves the universal claim; the proof in RESULT.md supplies the all-n and all-order argument. No external independent audit has been performed.
