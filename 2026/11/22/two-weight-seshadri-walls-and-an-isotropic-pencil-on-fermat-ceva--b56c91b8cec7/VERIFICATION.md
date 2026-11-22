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

# Verification record

The mathematical proof is contained in `RESULT.md`. The exact standalone consistency checker is `check.py` and uses only the Python standard library. Run it from this directory with:

```
python3 check.py
```

Observed result: `PASS: exact grid incidences, two-weight bounds, isotropic class, genus for m=2..40`.

The computation checks all modular incidence relations for integers from 2 to 40, uses rational arithmetic for representative weight rays, and verifies the divisor intersection and adjunction formulas. It neither replaces Bézout's theorem nor gives exhaustive singular-fiber information for the associated pencil. The proof of the infinite family relies on the uniform incidence count, two Bézout inequalities, local generators of the pencil, and standard intersection theory on a blow-up. Independent external validation has not been performed.
