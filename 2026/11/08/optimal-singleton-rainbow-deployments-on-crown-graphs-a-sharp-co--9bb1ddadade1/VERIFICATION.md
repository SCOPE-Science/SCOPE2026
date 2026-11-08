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

The file `artifacts/verify.py` can be executed with Python 3 using only its standard library. It constructs all \(2n\) vertex assignments of specified weight by choosing supports and distributing singleton named colors, tests the literal crown-graph neighbourhood condition, and checks minimum weights, complete types, and exact counts. The replay was performed on the final candidate script, with the following end markers:

```
CROWN_OK 4 3 min 6 functions 792 types {'one_full': 648, 'matched': 144}
CROWN_OK 5 3 min 6 functions 900 types {'one_full': 540, 'matched': 360}
CROWN_OK 6 3 min 6 functions 900 types {'one_full': 180, 'matched': 720}
EXACT_INTEGER_COUNT_BOUNDARIES_OK
VERIFY_OK
```

This experiment is finite: \(k=2\) with \(n\le8\), \(k=3\) with \(n\le6\), plus arithmetic checks for a wider grid. The proof in RESULT.md is valid for all stated \(n,k\) and is not extrapolated from the code. Independent mathematical audit has not been performed.
