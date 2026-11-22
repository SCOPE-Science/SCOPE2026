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

The complete proof is in RESULT.md, including all-exponent local isometry and lifting arguments. Run `python3 verify.py` in the extracted directory with Python 3 and the standard library. The verifier independently computes seven falling-factorial value/derivative pairs, counts all residues in entire index periods for five prime-power levels, checks index-period obstructions at the first four levels, and verifies first-level surjectivity for all smaller primes. Its observed final line was:

```text
VERIFY_OK exact_assertions=19665 exponents=1..5 max_modulus=16807 local_table=7
```

Exact finite checks do not replace the infinite proof. No independent mathematical audit has been performed.
