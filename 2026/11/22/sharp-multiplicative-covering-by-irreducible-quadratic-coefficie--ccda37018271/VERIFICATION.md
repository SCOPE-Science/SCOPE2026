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

The finite checker `VERIFY.py` evaluates all stated sets by direct arithmetic, including quadratic extensions. Its recorded result was:

```
VERIFY_OK field_cases= 49 nonsquare_constants= 411
```

The general proof is analytic, not an extrapolation from finite testing. In particular, the critical excluded-product argument uses a smooth genus-one model of a quartic, rules out rational infinity points via its nonsquare leading coefficient, and applies the Hasse–Weil genus-one lower bound. The discriminant identity and the field-size inequalities are given explicitly in `RESULT.md`. Independent audit has not been performed.
