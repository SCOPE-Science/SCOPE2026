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

Run `python3 CHECK.py` using only the Python standard library. It constructs the finite self-ambiguity transform by direct complex summation, checks the branch formula and sharp optimizer in eight even orders, and tests 1,280 other amplitude/phase configurations. The observed output was:

```
CHECK_OK even_orders=8 direct_cases=48 random_phase_radius_cases=1280
```

These are floating-point consistency tests, not an exact computer-assisted proof and not a replacement for the all-order angular argument. Equality, positivity, uniqueness, normalization, and the excluded small orders are established in RESULT.md. No independent external audit has been performed.
