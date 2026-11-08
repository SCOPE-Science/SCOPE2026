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

The standalone file `verify_binary_run_mas.py` uses standard-library Python only. It constructs the actual minimal absent scattered-subsequence set by literal host subsequence membership and all one-letter deletions, independently constructs the same set using greedy bridge positions, and asserts equality for 25 parameter triples. It separately evaluates the recurrence for 4,056 triples of run lengths and repetition counts and compares it with the Fibonacci formula.

Observed output:

```
VERIFY_OK direct_vs_bridge_cases 25 total_minimal_absent_symbol_positions 2008 graph_cases 4056 first_six_counts [3, 8, 21, 55, 144, 377]
```

The finite computations are consistency checks rather than a proof of the theorem for every integer parameter. The general mathematical proof appears in `RESULT.md`. No independent audit or external certification has occurred.
