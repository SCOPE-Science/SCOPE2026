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

Run `python3 verify.py` in the directory containing this file and `verify.py` using a standard Python 3 interpreter. The replay checks direct, separately constructed exact-rational full grounded matrix inverses against the formula for every feasible follower allocation in nine finite parameter pairs; tests the minimizing allocation by complete budget-by-budget enumeration in those pairs; and evaluates the critical derivative bound for every indexed coordinate pair. The observed output is:

```
VERIFY_OK allocations=828 exact_inverse=828 optimal_budgets=66 derivative_checks=5082
```

The universal proof instead consists of the rank-one quotient identity, the strict derivative bound, and the terminating concentration argument in `RESULT.md`. Finite enumeration is not an infinite-size proof. The literature comparison is not a guarantee of publication priority. No independent mathematical audit has been performed.
