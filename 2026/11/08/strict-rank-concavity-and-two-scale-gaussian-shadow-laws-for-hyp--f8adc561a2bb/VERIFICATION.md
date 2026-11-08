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

# Verification

The accompanying Python script `verify_shadow.py` uses a fixed random seed, direct enumeration of all fixed-cardinality planar Gaussian sums, and SciPy convex hulls. It independently integrates the Gaussian score-tie/binomial expression (not the beta-quantile kernel) to obtain the theoretical vertex-count expectations.

The finite checks cover every rank for sizes 4, 6, and 8, with 500 random configurations each, and test strict finite differences in sizes 4, 6, 8, 20, 80 and 250. Executing `python verify_shadow.py` after extracting the files yielded `GAUSSIAN_HYPERSIMPLEX_SHADOW_FORMULA_AND_CONCAVITY_CHECKS_PASSED`.

The all-dimensional correctness argument is the deterministic top-rank crossing count, the beta order-statistic comparison of consecutive first differences, and the beta/Gaussian tail estimates. Finite tests do not establish these limits or exclude an unseen priority-equivalent formulation. This is self-review only, not an independent audit.
