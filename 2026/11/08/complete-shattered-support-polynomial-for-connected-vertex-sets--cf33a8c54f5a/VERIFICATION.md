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

# Verification evidence

The supplied standalone `theta_verify.py` uses only Python 3 standard library. Running `python theta_verify.py` completes successfully and prints:

```text
DIRECT_CONNECTED_SUBSETS_PASS 6680
ALL_THETA_ARMS_1_TO_4_PASS 45740
THETA_CONNECTED_SHATTERING_PASS
```

The first phase enumerates all connected induced vertex subsets, plus the empty set, and compares all traces against the stated support criterion on tested theta graphs with no more than ten vertices. The second phase independently tests pairwise reachability after deleting other support vertices for every arm-length triple in \(\{1,2,3,4\}^3\) and all candidate supports through size five, then checks the coefficient polynomial.

The general theorem is proved symbolically in `RESULT.md`. Finite testing does not certify untested infinite parameter ranges. No formal-proof-assistant or independent external audit evidence is asserted.
