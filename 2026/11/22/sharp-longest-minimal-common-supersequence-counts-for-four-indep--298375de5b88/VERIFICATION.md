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

The main statement is proved for every positive integer quadruple by the canonical-embedding and central-gap arguments in `RESULT.md`. The additional checks are reproducible finite instances; none is substituted for the infinite proof.

Run from this document's directory:

```sh
python3 verification/exhaustive.py
python3 verification/constructive.py
```

The recorded outputs are `verification/exhaustive_output.txt` and `verification/constructive_output.txt`. They verify the strict one-symbol length bound in the exhaustive parameter range, both types' noncollision, actual deletion-minimality, and all parameter-boundary cases through five. Python 3's standard library is sufficient. Independent external review has not been performed.
