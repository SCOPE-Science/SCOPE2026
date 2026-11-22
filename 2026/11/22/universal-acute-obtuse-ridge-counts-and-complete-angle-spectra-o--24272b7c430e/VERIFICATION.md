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

Run `python3 ridge_checker.py` using Python 3 standard library. The exact arithmetic checker builds every edge vertex, tests all pairs of supporting facets through affine-rank elimination, and separately checks the squared normalized Gram products and their signs. Observed output:

```
MULTIPARTITE_EDGE_RIDGE_PASS profiles=6 ridge_pairs=603 nonridge_pairs=24
```

Checked part-size profiles: `(3,3,3)`, `(3,3,4)`, `(3,4,5)`, `(4,4,4)`, `(3,3,3,3)`, `(3,3,4,4)`. The checker covers only these finite profiles; the universal statement is established analytically in RESULT.md. No independent audit has been conducted.
