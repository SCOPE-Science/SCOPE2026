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

# Verification of the stated correlation theorem

Run `python3 verify.py` with Python 3 and its standard library. This enumerates all cyclic lag cross-sums for \(L=1,\ldots,11\), checks every one against the independent carry-matrix evaluation, and checks the exact rational limiting expression for all positive shifts below \(4096\). It also checks the sharp bound/equality cases and the alternating-shift recurrence through \(m=14\). Observed result from execution of the packaged checker:

```
VERIFY_OK checked_cyclic_lag_pairs=5592404 max_levels=11 bound_shifts=4095 alternating_m=14
EXAMPLES {0: '1', 1: '2/3', 2: '2/3', 3: '8/15', 5: '12/25', 7: '12/25', 11: '152/375', 21: '664/1875', 43: '2848/9375'}
```

The sum of direct products is an exact finite check, not an infinite certificate. The proof in `RESULT.md` gives exact matrix identities and the deductions for all \(L\) and all fixed shifts. No independent audit has been performed.
