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

Run `python3 verify.py` using the Python standard library. The checker tests the exact cubic derivative identities at all four corners of the relevant slope-derivative square, the exact bump extrema, the rational near-plateau witness formula for six positive rational perturbations, and numerical total variation over the real critical points of every cubic difference for 3,200 pseudorandom finite input pairs.

Expected terminal markers:

```text
EXACT_HERMITE_CORNER_NONNEGATIVITY_POLYNOMIALS_PASS
EXACT_SIDE_BUMP_EXTREMA_AND_SHARP_GAIN_PASS 59/27
EXACT_RATIONAL_NEAR_PLATEAU_SHARPNESS_PASS
INDEPENDENT_CUBIC_CRITICAL_POINT_NUMERICAL_STRESS_PASS 3200
ALL_HARMONIC_HERMITE_VARIATION_CHECKS_PASS
```

The unrestricted claim is supported by the five-step written proof in `RESULT.md`. In particular, the finite tests do not establish the all-sequence Lipschitz inequality and no numerical sample is claimed to attain the limiting sharp gain. The historical-priority comparisons depend on accessible published sources and are not an independent audit.
