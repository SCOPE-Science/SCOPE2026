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

Execute `python3 verify_ciani11.py` with Python 3 (standard library only).

Expected terminal report:

```
F121 smooth= 14043 p_ranks= 25 326 560 13132 A_zero= 351 B_zero= 585
F11 smooth= 73 p_ranks= 9 14 18 32 A_zero= 23 B_zero= 27
CIANI_F11_25_REDUCED_SUPERSPECIAL_POINTS_VERIFIED
```

The program expands the quartic to the tenth power by multinomial coefficients and compares the relevant terms with the proposed formulas. It checks all parameter pairs in both specified finite fields, enumerates all 25 geometric intersections by explicit formulas, and checks the smooth locus. Transversality over an algebraic closure is proved by the polynomial substitution and simple-root argument in RESULT.md, not by finite enumeration alone. It does not independently certify historical priority, all Newton polygons, or isomorphism class counts. Independent audit has not been performed.
