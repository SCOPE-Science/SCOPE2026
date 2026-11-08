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

# Reproducible finite checks

Run `python3 verify.py` with Python 3 standard library and enough memory for a list of 30001 integer central Delannoy numbers. The checker calculates the exact three-term recurrence and compares it with the direct binomial sum for indices zero through 100. It verifies complete value spectra at the first five powers of three, 201 sparse-block instances, the two seed congruences for eight valuation levels, principal-unit generator checks through the sixth power, and candidate constructive products for all admissible classes through the sixth power. A successful run prints the deterministic `VERIFY_OK` summary below.

```
VERIFY_OK exact_recurrence_n=0..30000 direct_binomial=101 complete_residue_levels=1..5 block_lemmas=201 signed_seed_levels=1..8 generator_levels=1..6 constructive_residue_levels=1..6
```

These are finite checks only, not a proof for every modulus. The infinite quantifiers depend on the symbolic polynomial, binomial, and valuation arguments in RESULT.md. No independent audit was conducted.
