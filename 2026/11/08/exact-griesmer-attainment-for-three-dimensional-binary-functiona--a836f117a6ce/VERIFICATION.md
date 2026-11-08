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

# Verification of the mathematical claim

Use Python 3 (standard library only):

```sh
python3 checker.py
```

Place `checker.py` and `recovery_certificates.json` in the same directory. A correct replay prints six per-case lines and `PASS: 1260 exhaustive finite request instances; all recoveries independent/disjoint`. Every certificate includes column-index bit masks for all 7, 7, 28, 84, 210, and 924 request instances of its designated type, and each mask's XOR is independently recomputed by the checker. The checker also verifies all six matrices have binary rank three. The case for two-request functional PIR uses repeated requests, whereas the other five blocks cover every possible multiset of the stated size.

The general integer formula is not obtained from finite sampling. It follows from the finite block certificates plus the concatenation proof in `RESULT.md` and the classical Griesmer lower bound, with a separate proof that four columns cannot serve every two-request mixed functional batch.

The stated method is an directly reproducible finite exact certificate check, not independent external mathematical certification. No assertions are made about dimensions other than three or fields other than the binary field.
