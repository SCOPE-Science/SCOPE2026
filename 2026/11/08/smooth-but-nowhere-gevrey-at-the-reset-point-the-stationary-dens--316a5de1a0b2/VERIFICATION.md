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

# Verification scope

The analytical proof is contained in `RESULT.md`. It uses the explicitly stated Fourier-product decay and the stationary forward equation to obtain arbitrarily many derivatives, then a finite odd-factor product to derive the exact jet and growth. The closed-form density series used for off-origin analyticity and normalization is credited to the published partial-resetting literature.

`verification/verify_density.py` requires Python 3.9 or later and `mpmath` 1.3 or later. Running `python verification/verify_density.py` returned:

```
PASS: 56 symbolic-product and Fourier-integral diagnostic assertions
```

The tests compare the Fourier and pointwise series representations at two contraction ratios, numerical derivatives through order eight, the all-order recurrence through twelve consecutive indices for each ratio, and finite geometric-product values. These finitely many checks do not establish infinite differentiability, analytic continuation, or non-Gevrey regularity; those properties are proved analytically. No independent external audit has been performed.
