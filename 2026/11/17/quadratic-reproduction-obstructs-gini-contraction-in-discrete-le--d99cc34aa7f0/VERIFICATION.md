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

# Reproducibility and checks

Run `python3 polynomial_gini_verifier.py` with an ordinary Python 3 interpreter; no third-party libraries or network are required. This program calculates the polynomial projectors from exact Gram matrices and validates all tested identities with rational arithmetic.

Observed output:

```
EXACT_FOUR_SITE_SHARP_NORM_17_OVER_15_PASSED
EXACT_ALL_POLYNOMIAL_DEGREE_CASES_PASSED 36
EXACT_ALL_BOUNDARY_DEGREES_AND_BINARY_CUTS_PASSED
QUADRATIC_ENDPOINT_RATIO 20 1481/1045 1.4172248803827752
QUADRATIC_ENDPOINT_RATIO 50 79719/54145 1.472324314341121
QUADRATIC_ENDPOINT_RATIO 100 1267943/849915 1.4918468317419977
QUADRATIC_ENDPOINT_RATIO 250 469949/312495 1.5038608617737883
EXACT_CONTINUUM_INTEGRAL_189_OVER_125_PASSED
ALL_POLYNOMIAL_GINI_CHECKS_PASSED
```

The standalone proof is in `RESULT.md`: exact reproduction moments, a sign-change argument, the affine exception, and a Riemann-integral limit. Exhaustion through eleven nodes does not establish the unrestricted theorem, and the computed ratios do not establish the limit without the analytical argument. No independent mathematical audit has been performed.
