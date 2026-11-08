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

The proof is a complete symbolic argument over all positive integer shore sizes and all nonnegative real reward weights; its key algebra is displayed in `RESULT.md`. `verify.py` uses only the Python standard library and independently enumerates weighted crossing pairs and full agent-partition utilities to test the theorem at exact rational weights. Running `python3 verify.py` produced:

```
PASS: cut thresholds agree with independent pair-by-pair exhaustive cuts
PASS: full set partitions match sharp threshold for every tested model, including boundaries
PASS: 374353 threshold comparisons and 85922 exact agent-partition payoff comparisons
K_1,5: 4 K_4,4: 6/5 K_2,10: 6
```

Checks are finite and are not treated as substitutes for the proof. No machine-checked formal proof and no independent external validation are asserted.
