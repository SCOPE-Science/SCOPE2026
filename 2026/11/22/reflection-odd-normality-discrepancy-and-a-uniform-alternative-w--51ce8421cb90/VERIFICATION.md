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

# Verification record

`CHECK.py` is self-contained apart from the declared `mpmath` Python dependency. Execute `python3 CHECK.py` from the directory containing the file. The checker tests the exact identity for 18,443 algebraic and numerical assertions using finite rational samples, the exact uniform projection and variance, the Gaussian conditional expectation, and high-precision quadrature for the Gaussian reference variance and uniform alternative rejection limit.

Actual execution output:

```
checks: 18443
gaussian variance: 0.44233111437756269142232991582315
uniform variance: 1/7
uniform limiting 5-percent rejection: 0.000563036470104841576242212393706
```

The printed checks are deterministic consistency tests, not proofs of assertions for all sample sizes or all parent laws. The general reflection identity is proved by algebra, and the population blindness/central limit theorem by symmetry and U-statistic projection as written in `RESULT.md`. The Gaussian constant is expressed exactly as a convergent integral; its decimal representation comes from reproducible numerical quadrature. There has been no independent audit.
