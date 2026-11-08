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

# Verification and reproducibility

Execute `python check.py` from the directory containing this file and `check.py`, with NumPy and SciPy available. The checker reconstructs the analytic two-dimensional trace, compares actual eigenvalues of the symmetric preconditioned system for random positive-definite instances, tests the optimum against a dense scalar grid, verifies the nominal inverse-scale comparison, and evaluates Gaussian probabilities against \(F\)-distribution tails. The observed successful completion printed `VERIFY_OK 2234 exact-rational/numeric configurations, 5 Gaussian distribution checks` and `VERIFY_FIXED_SCALE_AND_OPTIMAL_FORMULA_OK`.

This evidence contains finite independent exact-rational/numerical cross-checks, not an exhaustive proof over dimensions or parameters. The infinitely quantified statements, strict boundaries and limiting probability are proved analytically in RESULT.md. No external independent mathematical audit or validation has been performed.
