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

# Verification and reproducibility

Run `python verify.py` using Python 3.9 or later and the standard library only. The packaged run returned:

```
PASS: 2764 deterministic exact-rational and physical-transform checks
```

The exact-rational checker builds bilateral moments of distinct positive rational nodes and weights, verifies the singular/positive Hankel dichotomy for \(K=1,2,3,4\), computes annihilating polynomials and positive weights, and tests the complete moment recurrence. The independent forward-response checks compute Brownian discounted boundary transforms, the mean absorption time and the left arrival probability for multiple source configurations and \(K\le5\), then reconstruct the predicted positive and negative exponential source moments from the observables.

The infinite-dimensional certificate is proved by the positive moment-Gram square identity and the finite-root property of nonzero polynomials. The lower bound on the number of observed rates follows from an open-parameter-dimension obstruction and invariance of domain. Neither a finite code test nor simulation certifies these global mathematical arguments.

No assertion is made about noisy data, numerical conditioning, an independent third-party audit or practical source-estimation rates. All first-public dates refer to the first accessible public preprint version rather than later journal publication.
