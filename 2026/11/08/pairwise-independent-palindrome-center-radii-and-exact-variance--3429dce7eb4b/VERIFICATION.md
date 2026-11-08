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

# Reproducibility checks

Run `python3 verify.py` with Python 3 (standard library only). The expected output is:

```
VERIFY_OK forest_checks=24668 brute_variance_cases=27 gf_cases=474
```

The implementation tests the reflection-forest property for every pair of admissible positive palindrome radii at distinct centers for lengths from 2 through 16. It then independently computes the entire distribution of the palindrome-occurrence count for all words with \(q=2,n\le12\), \(q=3,n\le8\), and \(q=4,n\le7\), comparing exact Fraction variances to the theorem. It separately generates exact rational coefficients of the stated variance generating function for \(q=2,\ldots,7\) and lengths 1 through 79. These finite checks supplement the complete forest and geometric-series proof in RESULT.md; they do not imply infinite validity by themselves.

The residual limitation is possible historical priority under different terminology. The exact theorem does not describe joint dependence of three or more centers (indeed joint independence is false).
