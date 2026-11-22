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

The finite-state programs in this package use standard Python 3 only. In one directory with all accompanying source files, execute:

```
python3 check_bitmask.py > observed_bitmask.json
python3 check_tuples.py > observed_tuples.json
```

Both programs independently construct the Petersen disjoint-edge neighborhoods and follow each legal pinned initial state until the first repeated state. `check_bitmask.py` uses ten-bit masks and counts all 120 three-pin patterns, the 45 two-pin patterns, and ten single-pin configurations. `check_tuples.py` uses direct ten-entry tuples and another alphabetic graph representation; it independently classifies all 120 triples, including all 15,360 compatible states, then checks forcing triples and pair-extension obstructions.

Compare the parsed JSON values of `observed_bitmask.json` with `bitmask_results.json`, and `observed_tuples.json` with `tuple_results.json`. Both original outputs include `"all_assertions": "passed"`. The human proof of minimal forcing uses monotonicity and explicit seed-only trajectories; exact basin populations depend on complete finite enumeration, not infinite-case inference. The two implementations do not constitute an independent external mathematical review.
