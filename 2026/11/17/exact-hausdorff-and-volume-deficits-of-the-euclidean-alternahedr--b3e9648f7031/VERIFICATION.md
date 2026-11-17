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

Execute `python check.py` with Python 3, NumPy, and SciPy. The check rebuilds permutation coordinates, parity classes, rational closest-point weights, the supporting inequality in every tested instance, and independently solves convex-hull volumes for \(3\le n\le6\). It also evaluates random generic integer directions by brute-force parity-constrained permutation maximization. The reported successful run was:

```
n=3 volume_ratio=0.500000000000000 predicted=0.500000000000000 facets=3
n=4 volume_ratio=0.875000000000000 predicted=0.875000000000000 facets=20
n=5 volume_ratio=0.979999999999999 predicted=0.980000000000000 facets=90
n=6 volume_ratio=0.997685185185171 predicted=0.997685185185185 facets=422
ALTERNATING_PERMUTOHEDRON_PASS exact_permutations=5910 width_trials=600 cartan_orders=199 hull_orders=4
```

The exact statements for all \(n\ge3\) are established by the cut-decomposition, determinant and projection proofs in `RESULT.md`. Finite hull computations are supporting tests, not an infinite classification. The earlier published alternahedron face description and parity rearrangement are credited. A complete external specialist audit and exhaustive historical-priority examination have not occurred.
