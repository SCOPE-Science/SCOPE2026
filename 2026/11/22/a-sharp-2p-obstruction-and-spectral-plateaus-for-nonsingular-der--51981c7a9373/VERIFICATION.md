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

The theorem is proved by the generator-parametrization, integral Lyndon multigrading, and exact rational-canonical matrix enumeration detailed in `RESULT.md`. The computational tests are separate sanity checks, not substitutes for the proof.

To replay, run:

```sh
python3 verify_free_lie_spectrum.py
python3 verify_extension_fields.py
```

The first script constructs each degree of the free Lie algebra as commutators in the two-letter tensor algebra, solves for its independent Lyndon basis, computes the induced derivation determinants, and tests all generator matrices over prime fields of orders 2, 3, 5 and 7 through the stated degrees. It ends with `FREE_LIE_MODULAR_DERIVATION_CHECK_OK`.

The second script performs independent quadratic-extension field arithmetic for all generator matrices over fields of orders 4 and 9, testing the resultant obstruction and closed census. It ends with `FREE_LIE_EXTENSION_FIELD_CHECK_OK`.

Results include the all-matrix vanishing at class four in characteristic two and at class six in characteristic three, as well as a plateau in the positive counts below those thresholds. The scripts cannot exhaust arbitrary \(q\) or \(c\); only the symbolic proof establishes the general statements. There is no independent expert or formal proof certification.
