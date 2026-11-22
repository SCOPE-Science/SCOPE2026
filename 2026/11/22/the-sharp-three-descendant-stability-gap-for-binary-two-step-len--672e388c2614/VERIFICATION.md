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

The exact proof is in RESULT.md. Reproduce all exhaustive and run-template checks with:

```sh
python3 verify_bruteforce.py
python3 verify_normal_form.py
```

Both programs are standalone and use only the Python standard library. Exact binary sources through length 12 are exhaustively checked; both endpoint run-template languages are checked against direct two-step generation through length 60. No finite run establishes the claim for larger lengths; the argument in RESULT.md supplies the all-integer proof. No external independent audit has been performed.
