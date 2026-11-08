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

# Reproduction and limits

Run `python verify.py` in a directory containing this file, `RESULT.md`, and `verify.py`. Only the Python standard library is required. The recorded output in `verification-output.txt` is:

```
PASS: 1471 deterministic coefficient, asymptotic and exact-symmetry checks
Analytic proof establishes all fixed-matrix small-perturbation assertions.
```

The script makes exact rational coefficient checks and finite, deterministic angular sampling checks of the nonlinear one-dimensional Gaussian transport integrand. The analytic derivation in `RESULT.md`, especially the uniform small-perturbation expansion and the exact angular moments, is required for the universal conclusion. The script does not establish an infinite theorem by enumeration and does not cover the omitted transition-boundary or scalar-difference cases.
