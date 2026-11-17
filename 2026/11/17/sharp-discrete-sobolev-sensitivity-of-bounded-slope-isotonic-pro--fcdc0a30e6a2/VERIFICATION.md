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

# Computational checks and limits
The included `verify.py` uses Python's standard-library exact rational arithmetic. Execute with `python verify.py` after extracting the package. The output includes exhaustive partition checks for lengths 2 through 10 (1013 nontrivial partitions), 400 exact finite-dimensional KKT projections, 200 exact two-input inequalities, and 33 exact strictly complementary sharp witnesses through length 34.

The verifier independently checks the row-sum and column-sum estimates, the two-block squared-norm identity, and all witness ratios. For arbitrary cap vectors, the unrestricted upper bound is certified by the analytic nonnegative-matrix estimate and full-dimensional affine-cell decomposition in `RESULT.md`. No finite test is asserted to prove arbitrary dimension, every real signal or continuous dependence on arbitrary positive caps.

This package has received only self-review. No independent audit is claimed.
