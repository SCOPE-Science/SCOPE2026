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

# Reproducibility and limitations

Execute `python3 verify.py` using the Python standard library. Its finite enumeration covers all unordered triples for moduli \(2\) through \(60\), with first-eleven moment signatures, and the explicit critical witnesses at prime powers. The observed result was:

```
VERIFY_OK moduli=2..60 unordered_triples=595664 tested_powers=1..11 hensel_levels_3adic=2..7 dyadic_levels=2..13 large_prime_witnesses=24
```

The proof in `RESULT.md` establishes the theorem for all moduli, while the executable checks only the stated finite cases. The program does not certify literature priority, the infinite theorem, or an independent audit.
