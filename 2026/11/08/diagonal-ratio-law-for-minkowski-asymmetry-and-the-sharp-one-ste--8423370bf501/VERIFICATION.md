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

The mathematical proof consists of a four-facet support-function translation, a nonnegative linear-dependence lower certificate, an explicit feasible minimizing center, and the tent-shaped section profile of a triangle. All assumptions and parameter boundaries appear in the main result.

Run the embedded standalone file with Python 3:

```
python check_asymmetry.py
```

It was executed against the actual embedded source text using Python's exact `fractions.Fraction` arithmetic. Observed output:

```
EXACT_QUADRILATERAL_ASYMMETRY_CERTIFICATES_OK 11724
BOUNDARY_AND_SHARP_CASES_OK
```

The checker verifies all four facet supports and both matching optimality certificates for 11,724 parameter pairs on rational grids, plus five hand-specified endpoints and transitions. This is not exhaustive over real numbers; no independent audit or infinite formal certification has been performed. The analytic proof covers every real parameter and handles the singular symmetric endpoint separately.
