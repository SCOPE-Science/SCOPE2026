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

# Mathematical reproducibility and scope

Run `python3 verify_metric_trees.py` with the standard Python library. It enumerates every labeled tree on at most five vertices by Prüfer codes and a deterministic selection of six- and seven-vertex trees. For every vertex of every test tree it independently solves the exact-rational Kirchhoff equations, forms a continuous quadratic Green solution on edges, computes its gradient energy, and compares with the subtree-cut evaluation. It also checks leaf localization and the exact star/path equality cases. The observed output was:

```text
EXACT_INDEPENDENT_QUADRATIC_GREEN_COMPARISONS_PASSED 1870
TREE_EXTREMAL_BOUNDS_AND_EQUALITY_CASES_PASSED 325
ALL_UNIT_TREE_SOBOLEV_CHECKS_PASSED
```

The implementation uses rational arithmetic, with no floating-point tolerances. It does not enumerate all trees of arbitrary size and is not an infinite proof. The proof for all finite trees uses Cauchy–Schwarz, path Fubini, the point-evaluation resistance identity, exact edge profiles, and a rooted-tree induction. The continuum point-location and equality classifications are proven analytically, not inferred from the checked finite sample. Independent audit has not been performed.
