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
# Verification notes

Run `python3 verify_rule22.py` in the directory containing this file and the script; only Python 3 is required. The verifier rebuilds both adjacency relations from the local cellular rule, checks the matrix stabilization identity, checks the complete 125-entry capped-gap certificate against an independent expected table, and verifies the all-length algebraic gap classification symbolically over gap lengths through 60.

The direct independent run on actual finite ring source words (not using the transfer relations to generate them) covered every source word of lengths 3 through 17, or 262136 source words, and compared target reachability for all target outputs with at most three ones. The exact run output was:

```
VERIFY_OK capped_cases=125 ring_lengths=5..60 gap_cases=34136 direct_inputs=262136
```

This is not a machine-checked infinite mathematical proof. The general claim relies on the exact Boolean trace equivalence, matrix identity \(B_0^4=B_0^5\), a complete finite capped table and orbit counting in `RESULT.md`. The independent audit state is unperformed.
