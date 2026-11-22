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

The standalone `checker.py` was run using Python 3 with standard-library fractions, factorials and explicit perfect-matching enumeration. Output:

```
n 1 pairings 1 checks 2
n 2 pairings 3 checks 10
n 3 pairings 15 checks 23
n 4 pairings 105 checks 47
n 5 pairings 945 checks 91
n 6 pairings 10395 checks 167
PASS 168 exact checks
```

The checker tests the rational simplex-integral probabilities, edge means, edge–isolation covariances, left/right occupancy distribution and conditional edge-count convolution for every pairing up to six intervals. The enumeration uses each perfect matching of the ordered endpoints with equal weight; taking every chord in turn as the distinguished vertex implements a uniformly marked label. Additional exact sign comparisons through 49 intervals use the derived sum formulas.

The general argument in `RESULT.md` uses the Dirichlet simplex integral, affine invariance and independence of uniformly distributed endpoints on disjoint subintervals, the exact ratios of factorial weights, and dominated convergence near boundary corners. These analytic steps, rather than a finite test, support the infinite result. The stated \(O(n^{-2})\) remainder in the mixed-side probability is an asymptotic order, not an experimental error bar. Independent review has not been performed.
