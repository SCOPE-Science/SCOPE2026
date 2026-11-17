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

# Reproduction and limits

The sole auxiliary dependency is a Python 3 interpreter with its standard library. Run `python3 verify.py` in the folder containing `verify.py`. The observed output was:

```
PASS exact assertions: 1756025
Brute vertex-pair dimensions: N=3,...,10; class-size/intersection dimensions: N=3,...,44
```

The implementation forms the complete two-level vertices using exact fractions, checks every candidate pair in dimensions \(3\le N\le10\), and tests all allowable cardinality/intersection classes in dimensions \(3\le N\le44\). It checks the stated number of unordered diametral pairs, the exact radius for every vertex, and the unique outer-shell cardinality. No floating-point tolerance is used. These are finite sanity checks, not an exhaustive computational proof for unbounded \(N\). The separate written argument proves the general statement via rational identities, monotonicity, strict convexity, and symmetry.

Exact metric normalization: the simplex is \(\operatorname{conv}\{e_1,\ldots,e_N\}\subset\mathbb R^N\) with its usual Euclidean metric; edge lengths are \(\sqrt2\). Relative volume statements, in contrast, are affine invariant. Independent mathematical audit has not been performed.
