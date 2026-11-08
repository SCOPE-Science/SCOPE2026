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

The included `CHECK.py` uses only the Python standard library and exact integer/fraction arithmetic. Execute `python3 CHECK.py` in the extracted file directory. Output observed:

```
TWO_INDEPENDENT_INTERSECTION_DEGREE_FORMULAS_OK 15
DUALITY_AND_LINE_PAIR_BINOMIAL_FORMULAS_OK
CHECK_OK
```

The first computation localizes the iterated projective-bundle pushforward over the rank-\(p+2\) Grassmannian. The second uses the Thom--Porteous determinant for the rank-degeneracy locus on a product of rank-\(p+1\) Grassmannians; it does not reuse the incidence-bundle summation. Both are exact over rational numbers. The script checks all \(15\) parameter pairs with \(3\le n\le7\) and \(1\le p\le n-2\), tests the duality symmetry, and independently checks the line-pair binomial expression. The computations cannot prove the infinite-range statement or historical originality; those rely on the general intersection-theoretic proof and comparison with primary literature.
