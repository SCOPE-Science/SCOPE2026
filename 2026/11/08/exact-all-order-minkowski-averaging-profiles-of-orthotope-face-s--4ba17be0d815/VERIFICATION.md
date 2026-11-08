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

# Reproducible checks and limits

Run `python3 checker.py` with Python 3 and only the standard library. Its actual deterministic result is:

```
PASS: 28065 exact assertions
```

The first check builds finite sums of discretized nonconvex cubical face points rather than assuming the closed-form grid-stratum identity. It tests all \(1\le n\le4\), \(0\le k\le n\), \(1\le N\le3\) on a half-grid. The second computes pointwise squared-distance minima over all possible subsets of coordinates constrained to a regular grid and compares these with the sorted-distance formula. The third uses positive unequal side lengths \((1,2,3)\), \((3,7,11)\), and \((1,1,5)\) and exact rational grid positions to check the anisotropic Euclidean Hausdorff upper bound and its simultaneous midpoint attainment. No floating-point comparison is involved.

The analytical proof independently establishes the full infinite statement by two-direction row allocation, coordinatewise nearest-grid minimization, and simultaneous midpoint maximization. Finite tests cannot establish all real inputs, all dimensions, or all \(\ell_p\) norms. No external proof-assistant certification or independent mathematical audit is asserted.
