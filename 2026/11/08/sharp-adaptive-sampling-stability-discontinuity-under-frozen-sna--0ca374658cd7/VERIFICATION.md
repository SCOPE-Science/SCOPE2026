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

# Reproducibility and mathematical verification

The only executable artifact is `CHECK.py`. Run it with Python 3, without third-party packages:

```sh
python CHECK.py
```

It printed `PASS: 7816 exact-enumeration and collision-product assertions` when executed from the extracted file. The test exhaustively enumerates all independent selection tuples for small dimensions and batch widths, uses rational arithmetic to compare conditional second moments exactly, checks the precise uniform factor and adaptive contraction, and compares the infinite-collision product's finite logarithmic approximation with its analytic lower bound.

Its exhaustive testing range is \(2\le m\le4\), with \(1\le T\le4\) for \(m\le3\) and \(1\le T\le2\) for \(m=4\); it tests five positive rational relaxation parameters, exponents \(\ell\in\{0,1,2\}\), and the nonzero coordinate vectors from \(\{0,1,2\}^m\). Separate finite logarithmic checks sample collision factors for batch widths \(T\in\{3,4,5\}\), positive exponents and four positive off-coordinate ratios.

The checker does not enumerate every dimension, exponent, start, batch history or infinite event. The global convergence and divergence conclusions depend on the mathematical proof, specifically multinomial marginal moments, a rearrangement inequality, a Borel–Cantelli argument and a convergent geometric-product bound. There is no independent mathematical audit or external formal certification.
