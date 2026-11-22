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

The analytical proof in `RESULT.md` establishes the theorem for every finite abelian factor group and every exponent strictly between one and infinity. The decisive steps are characterization of the additive Fourier image, strict convexity and group symmetry, an exact two-variable stationarity calculation, character inversion, and monotonicity of the intersection numerator.

`python artifacts/check_cross.py` ran successfully with Python standard library only and printed:

```
PASS: 4768 supplementary evaluations; all-p, all-group proof is analytic.
```

The checks cover direct transform levels and their multiplicities on finite cyclic examples, equality ratios, the Parseval normalization, random complex perturbations, and a critical-exponent example. The code checks a finite collection of instances; it does not replace the all-orders, all-exponents proof. No machine-checked formal theorem, external audit, numerical noise bound, or endpoint result is asserted. A broader historical literature search could reveal an earlier equivalent additive-product minimization.
