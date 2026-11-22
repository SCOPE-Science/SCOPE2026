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

Run `python verify_odd_cycle.py` with Python 3. The program tests actual signed-root facet Gram determinants and exact balanced-bridge squared norm values, both as integers, for all \(98\) balanced sign words in odd lengths \(3,5,7,9\); rotating the missing edge accounts for \(806\) facets. It also checks the predicted exact mean squared area for each dimension. Recorded output:

```
n=3: facets=6 distinct_squared_area_classes=1 exact_mean=2
n=5: facets=30 distinct_squared_area_classes=3 exact_mean=5/18
n=7: facets=140 distinct_squared_area_classes=6 exact_mean=7/3600
n=9: facets=630 distinct_squared_area_classes=12 exact_mean=1/423360
ODD_CYCLE_FACET_AREA_EXACT_PASS facets=806 n=3,5,7,9
```

A separate convex-hull computation was also used during derivation to check the facet distributions for the same dimensions (floating point); the exact deterministic checker supplied here is the reproducible certificate. The infinite odd-cycle family follows analytically from the facet bijection, the incidence determinant, exchangeable bridge signs, functional invariance and the Gaussian Fourier calculation. Exact finite tests alone do not establish the asymptotic law. No external independent audit has been performed.
