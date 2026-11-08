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

# Reproducibility and verification

Run `python rooted_forest_chain_moments_checker.py` with Python 3. The checker uses only the standard library; it does not depend on a scientific computing package. Its observed result on the packaged source was:

```
ROOTED_FOREST_CHAIN_MOMENTS_EXACT_PASSED 873 59602 34406 24328
```

The four counts are all increasing-label rooted forests up to order six, the combined number of canonical order-polytope simplices, rational first/second moment comparisons, and strict sign checks. The method is independent of the beta Jacobian proof: for every linear extension it writes each chain coordinate as a sum of disjoint or overlapping spacings of uniform order statistics. Exact Dirichlet spacing means and second moments integrate each simplex. Every simplex has the same Euclidean volume because the parent-difference transfer is unimodular. The program compares the resulting rational averages to the product moments and the complete covariance sign table.

These are finite exact checks, not an independent mathematical audit or infinite proof. The theorem is proved in `RESULT.md` by an explicit inverse transformation, exact Jacobian, beta integration, and a strict telescoping ratio inequality. Its limits include the rooted-forest hypothesis and historical-priority uncertainty.
