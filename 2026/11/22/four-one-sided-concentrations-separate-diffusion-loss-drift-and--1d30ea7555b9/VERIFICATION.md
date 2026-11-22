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

# Mathematical and computational verification

The full proof is in `RESULT.md` and rests on an exact decaying point-source Green function, two quadratic characteristic identities, strict monotonicity of the reconstructed amplitude ratio, and an explicit underdetermined family for three readings.

Run `python3 verify.py` with the standard library. The packaged source has been executed with output:

```
PASS: 120012 assertions: exact-rational witness, 12,000 seeded forward/inverse cases, PDE and jump identities, and an explicit three-reading ambiguity.
```

The rational witness checks \((D,\lambda,w,Q)=(1/2,3,3/2,7)\) exactly. The random tests verify numerical inversions for positive coefficients and drifts of either sign, and check the characteristic and source-jump equations. The final test changes a rate while preserving three observations. These finite checks do not prove the global theorem; the proof is the exact algebra and strict inequalities in `RESULT.md`.

Limits: validation assumes exact four-scalar observations of two different equilibrated states and a common constant source. No stability under observational error or validity for genuinely time-dependent tidal fields was assessed. Independent external validation has not been performed.
