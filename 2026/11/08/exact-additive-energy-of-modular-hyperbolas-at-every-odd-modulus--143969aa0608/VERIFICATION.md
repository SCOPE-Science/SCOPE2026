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

# Reproducibility
Run `python3 verify_energy.py` using Python 3 standard-library facilities only. The complete finite check executed successfully with output:

```
VERIFY_OK local_moduli=16 composite_moduli=18 fixed_first_root_cases=1496
```

The verifier directly constructs all ordered pair sums of inverse-graph points, squares their multiplicities to obtain the additive energy, independently checks the fixed-first-index roots, and checks the multiplicative formula on composite odd moduli. The checked ranges are explicit in the program. No floating-point approximation or outside data is used. This finite validation cannot establish the unrestricted identity for every prime and exponent; that is proved algebraically in `RESULT.md`. Independent mathematical auditing has not been performed.
