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
# Reproducibility and limits

Execute `python3 verify.py` using Python 3. The verified run printed:

```
VERIFY_OK checks=87555
VERIFY_ZETA_OK total_checks=87651
```

The code independently enumerates finite binary cyclic languages, admissible periodic words, gap constraints, the positive Perron root equation, and exact adjacency trace counts. Checks cover cyclic marker periods 2–11 and selected adjacency dimensions 1–8. The mathematical classification for unbounded period and resolution is proved symbolically in `RESULT.md`; finite tests are not a certificate of all cases. Historical priority and independent external validation remain unperformed.
