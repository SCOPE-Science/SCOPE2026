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

# Reproducible checks

Run `python3 verify_septic_char2.py` (standard library only). It constructs Cartier matrices by extracting odd powers from the degree-three Kummer polynomial, performs inverse-Frobenius-semilinear multiplication over exact finite fields, and computes ranks by finite-field Gaussian elimination. An executed run printed:

```
t 2 seq (4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
t 3 seq (4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
GF 4 counts Counter({(4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0): 2})
GF 8 counts Counter({(4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3): 6})
CYCLIC_SEPTIC_CHARACTERISTIC_TWO_VERIFIED_OK
```

Over \(\mathbf F_4\), both smooth parameters are roots of \(t^2+t+1\) and have nilpotence index five. Over \(\mathbf F_8\), all six smooth parameters have stable rank three. These finite checks corroborate the universal symbolic proof; they do not prove it by sampling. Independent review has not been performed.
