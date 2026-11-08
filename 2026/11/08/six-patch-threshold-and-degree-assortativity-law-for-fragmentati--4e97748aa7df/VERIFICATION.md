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

Use Python 3.9 or later with only the standard library. Extract `verify.py` from this finding and execute:

```sh
python3 verify.py
```

The checker reports `EXACT_OK` and tests unlabeled Prüfer tree classes from two to six vertices, their degree/cumulant signatures, all occupied subsets for four rational survival probabilities, and the explicit six-vertex witness. All identities use rational arithmetic. The proof of the exact polynomial for *arbitrary* vertex counts and real probabilities is the independent-support third-cumulant calculation in `RESULT.md`, not an inference from finite evaluation. Independent audit is not performed.
