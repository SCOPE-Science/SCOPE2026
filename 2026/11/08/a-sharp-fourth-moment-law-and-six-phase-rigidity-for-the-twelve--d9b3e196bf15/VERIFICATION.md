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

# Reproducibility and scope

The proof of the unrestricted complex-phase inequality and the complete two-orbit equality classification is symbolic and self-contained in `RESULT.md`. The only computed assertions are the exact restricted-alphabet minima and optimizer counts for \(q=2,3,4,5,6\).

From the same directory as `checker.cpp`, run:

```sh
g++ -O3 -std=c++17 checker.cpp -o checker && ./checker
```

The observed completed output was:

```
q=2 states=256 min=188 normalized=3 total=48
q=3 states=6561 min=216 normalized=16 total=1296
q=4 states=65536 min=188 normalized=9 total=2304
q=5 states=390625 min=240-20sqrt(5) normalized=24 total=15000
q=6 states=1679616 min=180 normalized=2 total=2592
A3_FOURTH_MOMENT_EXACT_PASS normalized_cases=2142594
```

All moment minimizations are exhaustive over the eight unrestricted normalized exponent positions. For the fifth-root alphabet, the checker represents squared norms as exact \(\mathbb Z+\sqrt5\mathbb Z\) pairs and compares their signs using integer squaring. For all five witness arrays it computes the fourth moment both from difference autocorrelations and from the convolution coefficients of the square of the Fourier polynomial. This dual check is not a logically independent mathematical review. The proof applies to finite grids only when every coordinate order is at least five, so difference frequencies remain distinct; no smaller-grid assertion has been verified.
