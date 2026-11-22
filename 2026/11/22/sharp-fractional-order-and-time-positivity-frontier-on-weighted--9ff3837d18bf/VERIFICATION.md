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

# Verification details

The proof relies on elementary but exact spectral-projector identities on a weighted three-site Laplacian, a sign-ordering identity for the smallest and second-smallest conductances, a convexity argument giving a unique positive zero, and explicit spectral expansions for two singular parameter families.

The provided `verify_triangle.py` checks independent symmetric eigendecomposition and matrix-exponential evaluations against the derived expressions, includes explicit transient maximum-norm comparisons, and evaluates both singular-order asymptotics. The deterministic local run completed 20,272 assertions. Its output is not a proof for an infinite parameter range, nor an independent external audit. Reproduce with Python 3, NumPy and SciPy by invoking `python verify_triangle.py` in the directory containing the script.

All stated claims are restricted to real positive edge weights, real positive spectral orders, and nonnegative real times. No numerical search or finite enumeration is used to justify the exhaustive theorem.
