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

## Reproducibility

Run `python3 verify_connected_ladder.py` (Python 3 standard library only). The executable enumerates all vertex subsets of each open ladder from one to eight rungs; it decides connectedness by an independent depth-first search, then performs a direct integer Walsh–Hadamard transform. Every frequency is compared with the separate signed-state recurrence. The same script verifies the exact total-count formula, the periodic certificate through 400 rungs, and every step of the four-state block.

One execution passed 93,771 integer assertions. The exact unsigned totals at one through eight rungs were 3, 13, 40, 108, 275, 681, 1664 and 4040. The corresponding exact Fourier zero counts were 0, 0, 9, 66, 0, 0, 870 and 7462.

## Mathematical limits

The all-size proof rests on the stated recurrence and its four-state induction, not on this finite checker. No exhaustive computation beyond eight rungs is claimed. Neither the complete singular nullity nor conditioning on its nonzero range is asserted. Independent validation has not been performed.
