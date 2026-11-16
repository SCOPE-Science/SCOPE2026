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

Both supplied standard-library Python 3 programs are executable in the same directory as this file:

```
python3 tree_walsh_check.py
python3 tree_state_certificate.py
```

`tree_walsh_check.py` explicitly enumerates all 32,768 binary assignments on the 15-vertex tree, identifies all 2,306 independent sets, applies integer Walsh--Hadamard transforms and checks 32,768 independent recurrence evaluations. It checks height 0--3, exact Parseval sums, gaps and three-cycle witnesses. `tree_state_certificate.py` recomputes the exact state multiplicities, shows the only 14,402 zero combinations at height three occur with a negative root sign, and checks the explicit 12-state intermediate table and Parseval identity.

Successful actual runs returned `BINARY_TREE_WALSH_PASS` and `BINARY_TREE_STATE_CERTIFICATE_PASS`. The all-height statements are proved by the recurrence and parity construction in `RESULT.md`; no finite checker is asserted to certify infinitely many heights. The search for covering literature was bounded, and independent validation has not been performed.
