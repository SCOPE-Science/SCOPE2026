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

All-length deductions are contained in the structural classification and elementary area estimate in RESULT.md. No finite experiment is used as an induction or an infinite certificate.

Run `python3 verify_abelian_five_run.py` with Python 3 and no third-party packages. The checker independently enumerates actual literal contiguous factors and compares them with the claimed five-run count, as well as testing the extremal family. Expected output:

```
VERIFY_OK five_run_words=11628 grid_cases=16807 construction_cases=50
```

Verification covers lengths 5 through 19 exhaustively within the five-run family; run-length tuples in the independent grid range from 1 through 7; the construction identity is checked for 50 positive parameters. The upper-area bound and all-length limits are mathematical statements checked analytically, not by finite code.
