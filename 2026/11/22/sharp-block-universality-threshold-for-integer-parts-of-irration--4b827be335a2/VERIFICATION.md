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

# Reproducibility

Run `python3 check.py` alongside this file. The code uses only the standard Python library. It computes the exact integer parts of the sampling polynomials via `math.isqrt`, checks the degree-\(d\) finite-difference corrections for each sample, evaluates the independent weighted-uniform convolution with high-precision decimal arithmetic, and confirms the predicted correction-support cardinality modulo six moduli for each \(1\le d\le5\). It also tests the effects of a rational lower-degree coefficient perturbation. The executed run reported:

```
PASS: all-parameter support algebra for d=1..5 and 6 moduli; 198385 exact integer / distribution checks
First correction probabilities for d=2:
{1: '0.0073593128807148535949', 2: '0.3284271247461900976033', 3: '0.4926406871192851464050', 4: '0.1715728752538099023966'}
```

The probabilistic comparisons use a permissive absolute-frequency diagnostic tolerance to avoid asserting an unproved finite-prefix discrepancy estimate. The analytic proof of positive frequencies for all degrees rests on Weyl equidistribution, exact finite differences and a positive convolution density. The code does not establish the result for infinite parameter ranges and does not constitute an independent audit.
