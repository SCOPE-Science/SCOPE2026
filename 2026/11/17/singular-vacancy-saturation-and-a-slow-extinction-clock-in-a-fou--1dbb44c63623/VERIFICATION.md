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
# Verification notes

The equations and their origin are stated in `RESULT.md`. The analytical proof uses a conserved logarithmic vacancy expression at zero regular-conflict rate, uniqueness of its positive terminal root, Lambert-function asymptotics, and a finite weighted recruitment integral for small positive regular-conflict rate. These steps apply to the entire explicitly stated continuous parameter domain. The proof also establishes uniformity for scaled times bounded away from zero, but makes no joint two-parameter assertion.

Run `python verify_selection.py` (Python 3 with NumPy and SciPy). Observed output:

```
VERIFY_OK parameter_cases=3 exact_first_integrals=3 endpoint_selections=3 slow_scaled_samples=12 saturation_asymptotics=9
```

The script checks conservation, the first-integral identity, Lambert endpoint selection, twelve representative small-conflict scaled-time values, and nine exact/normalized strong-transfer asymptotic identities. These are numerical checks with solver tolerances and finite sample sizes, not a computer proof for all initial states, rates or times. No independent audit has been performed.
