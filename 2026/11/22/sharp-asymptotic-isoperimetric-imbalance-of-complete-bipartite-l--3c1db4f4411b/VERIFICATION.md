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

The file `check.py` creates the ordinary Laplacian of every complete-bipartite graph with \(3\le N\le10\), computes the intrinsic volume from an independent vertex-difference Gram determinant, computes each facet's intrinsic Gram-determinant volume, and compares all outputs to the analytic formulas. There are 44 tested \((p,q)\) pairs. The script then evaluates stable log-gamma versions of the exact isoperimetric quotient at \(N=100,200,400,800,1600,3200\), confirming approach toward the sharp implicit optimizer.

Run from a directory containing the accompanying source:

```shell
python check.py
```

Requirements: Python 3 and NumPy. Expected final marker: `BIPARTITE_ISOPERIMETRIC_PROFILE_PASS`; the direct metric test marker is `DIRECT_VOLUME_FACET_AREA_PASS`.

The infinite-dimensional correctness rests on the spectral volume identity, pseudoinverse facet-area identity, uniform Stirling approximation and exact sign analysis of the derivative; the finite checker is an independently computed stress test, not a substitute for those arguments. No independent external review has been performed.
