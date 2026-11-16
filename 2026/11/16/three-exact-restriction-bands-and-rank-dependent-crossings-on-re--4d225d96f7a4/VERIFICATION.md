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
# Verification

The analytical proof uses the unique \(O(n)\)-invariant quadratic covariance on trace-free symmetric matrices, the conditional Haar block identities, the Beta coordinate density, and three exact differentiated tail-polynomial identities. These identities prove the unrestricted integer-parameter theorem; finite computations are independent corroboration.

Run the standalone checker with `python checker.py` after installing the packages listed in `requirements.txt`. Its actual outputs were:

```text
GRASSMANNIAN_CAP_SYMBOLIC_PASS trace_and_three_crossings
GRASSMANNIAN_CAP_NUMERIC_PASS dimensions_rank_cases=10 thresholds=40
```

A separate direct Haar-projector experiment at dimension \(6\), rank \(2\), threshold \(0.4\), with 14,000 Gaussian-QR projectors, found empirical axial/cross/tangential concentration ratios approximately \((0.5921,0.4680,0.3090)\), versus the exact Beta values \((0.5904,0.4752,0.3024)\). This is statistical corroboration and is not part of the theorem's proof.

Checks do not enumerate all dimensions or masks, and the manuscript does not claim independent verification, external certification, or previously unknown Grassmannian harmonic decompositions.
