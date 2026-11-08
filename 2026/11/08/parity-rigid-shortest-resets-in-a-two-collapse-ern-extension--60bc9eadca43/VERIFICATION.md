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

# Reproducible checks

Run `python3 verify.py` with Python 3 and the standard library. The program constructs the alphabet maps directly from their definitions and performs subset-automaton breadth-first searches for all integer state sizes from 2 through 15. It records both shortest reset distance and total number of shortest reset words. For all state sizes 2 through 12, it additionally reconstructs the complete sets of shortest words and compares them with the two explicit word formulas. A separate endpoint/event-pattern calculation checks every minimal expansion span and number of placements from 2 through 50.

The actual program output was:

```
VERIFY_OK n=2..15 BFS, n=2..12 all shortest words, n=2..50 independent event DP; subset states: 65385
```

These exhaustive finite-state checks do not certify the theorem for unbounded state size. The universal result is justified by the reverse-interval and periodic-expansion proof in `RESULT.md`. There is no independent expert audit or machine-formal proof.
