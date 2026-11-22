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

# Verification record

## Actual computational checks

Run with `python3 verify.py` using only the Python standard library. The verifier is standalone and computes deletion outcomes directly from breadth-first search on unit-weight cycles and Dijkstra shortest paths on positive-integer weighted cycles; the success test does not invoke the terminal-gap characterization.

Observed output:

```
CYCLE_N_PASS 3 terminal_sets 4
CYCLE_N_PASS 4 terminal_sets 11
CYCLE_N_PASS 5 terminal_sets 26
CYCLE_N_PASS 6 terminal_sets 57
CYCLE_N_PASS 7 terminal_sets 120
CYCLE_N_PASS 8 terminal_sets 247
CYCLE_N_PASS 9 terminal_sets 502
ALL_ORDERS_DISTANCE_ENUMERATION_PASS 340304
LOG_CONCAVITY_AND_TOTAL_COUNTS_SAMPLE_PASS
VERIFY_OK
WEIGHTED_CYCLE_N_PASS 3
WEIGHTED_CYCLE_N_PASS 4
WEIGHTED_CYCLE_N_PASS 5
WEIGHTED_CYCLE_N_PASS 6
WEIGHTED_CYCLE_N_PASS 7
WEIGHTED_CYCLE_N_PASS 8
WEIGHTED_DIRECT_DISTANCE_ENUMERATION_PASS 333120
WEIGHTED_VERIFY_OK
```

The unweighted check ranges over every terminal subset of size at least two and every deleted-edge subset on cycles with \(3\le n\le9\), for 340,304 terminal/deletion tests. The weighted check uses four deterministic positive integer edge-length assignments on each \(3\le n\le8\), for 333,120 tests. For every tested terminal placement it compares the complete coefficient vectors, minimum cardinality and minimum-set count, not merely the total count. Additional selected coefficient log-concavity and total-count checks cover orders up to \(100\).

## Unrestricted argument and limitations

The proof in `RESULT.md` covers every \(n\ge3\), every terminal set of cardinality at least two, and every assignment of positive real edge lengths. Finite computation does not certify infinite quantifiers, historical originality, or independent validation. The weighted test uses selected integer length assignments, not all real length vectors; the all-weight conclusion follows from the gap argument rather than sampling. There is no independent mathematical audit.
