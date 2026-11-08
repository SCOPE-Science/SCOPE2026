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

The independent scientific audit has not been performed. The exact theorem was checked by reconstructing its branch cases and separately executing the standalone `hierarchy_check.py` with Python 3 standard library. Algorithm A applies a rank recurrence directly to induced ancestor posets; Algorithm B enumerates all binary label functions, retains the ancestor-closed assignments, and recurses on hypothesis-space splits. They agree for heights zero through three on concept counts and exact Littlestone dimensions; see `checker_output.txt`. Algorithm B evaluated 49,961 memoized hypothesis states in the largest case, and Algorithm A 8,597 induced-poset states. These finite exhaustive checks independently corroborate the h=3 value but do not establish any claim for higher heights. The published-source priority search did not certify novelty.
