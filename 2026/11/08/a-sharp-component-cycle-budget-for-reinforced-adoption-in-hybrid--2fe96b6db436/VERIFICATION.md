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

# Reproducibility and verification

Run `python verify.py` with Python 3.10 or later, without third-party packages. The script checks the component–cycle resource inequality by enumerating all connected simple labeled graphs with two, three, or four vertices and every admissible threshold vector and seed set. It independently enumerates all legal asynchronous activation orders in those cases and verifies that every terminal configuration equals deterministic closure. It then checks 20,000 pseudorandomly generated cases on larger connected graphs and 99 explicit sharp constructions.

Observed output from the included script:

```
PASS: component-cycle inequality 28336 independent finite instances
PASS: all asynchronous terminal states 8336 instances
PASS: sharp constructions 99 families, independent of activation rates
```

All tests ran on the exact supplied script. The universal proof uses edge accounting, not finite enumeration. The tests do not establish absence of covering published mathematics or provide an independent audit. The rate-independence statement requires every enabled transition to retain a strictly positive rate; a rate of zero is excluded.
