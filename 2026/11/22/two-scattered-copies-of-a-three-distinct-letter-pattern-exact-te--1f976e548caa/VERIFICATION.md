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

# Reproducibility

Run both standard-library scripts from the package root with Python 3:

```shell
python verification/verify_direct.py
python verification/verify_transfer.py
```

The first enumerates each ternary word through length eleven, checks the exact subsequence count and records the two possible positive-contribution patterns; it prints `DIRECT_OK`. The second uses a separately implemented prefix-state recurrence and checks coefficients through length fifty against the displayed rational function; it prints `TRANSFER_OK`.

The output files `verification/direct_output.txt` and `verification/transfer_output.txt` record the executions. Calculations are reproducible but finite; the proof of every length is the regular-language partition and generating-function computation in `RESULT.md`, not extrapolation. No external proof assistant or independent expert verification has been performed.
