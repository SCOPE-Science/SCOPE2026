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

# Reproducible verification

Install the packages in `requirements.txt`, then run:

```
python verify_split.py
```

The program constructs graph edge lists, selects every connected directed cut, independently enumerates all endpoint sums of generators retained on the exposed face, computes orthonormal intrinsic face coordinates using singular-value decomposition, and measures the convex hull in that subspace. It tests \(12+22+40+28+54=156\) facets in five complete-split instances, including the two nontrivial clique sizes and several additional boundary cases. The maximum per-facet numerical discrepancy in the tests was below \(3\times10^{-13}\) in the run used for this review.

The checker independently counts spanning trees by enumerating graph edge subsets, validating the required formula for four complete-split graphs. Stable binomial expectation calculations test the finite exact split-to-singleton surface ratio against the first asymptotic coefficient for selected larger parameter values. The expected terminal message is `SPLIT_SURFACE_PASS direct_facets=156`.

The all-dimensional identity and both limiting statements are proved in `RESULT.md`; finite checks do not constitute an exhaustive verification for arbitrary parameters or an independent mathematical audit. External independent review has not been performed.
