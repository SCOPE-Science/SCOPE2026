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

# Verification

Run from the directory containing the accompanying standalone script:

```sh
python3 CHECK.py
```

Requires Python 3 and SymPy. The output obtained on execution was:

```
symbolic_coefficients_verified
root_of_unity_orders_checked
finite_mode_pairs_checked 15000
```

The checker constructs the quartic Bernstein polynomial from the five symbolic values, tests the exact endpoint-derivative and zeroth-coefficient identities, and checks 15,000 positive-frequency cases plus finite cyclotomic orders up to 300. It does not certify the infinite-frequency statement. That statement is established analytically by the almost-periodic mean-square argument, a complete root-order case split, and signed polynomial cosine-coefficient formulas in `RESULT.md`. Strict-node hypotheses and all endpoint conditions are part of the theorem. No independent mathematical audit has been performed.
