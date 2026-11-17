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

Execute `python verify_rook_completion.py` in an environment with Python 3.10 or newer. Standard-library exact rational checks always run; if NumPy and SciPy are installed, the independent constrained least-squares optimizer also runs.

The tested block formula covers every rank at all dimensions \(2\le n\le7\). Each candidate is checked for nonnegativity, all row/column sums, the exact target squared distance, and the inner-product projection inequality against every permutation matrix, giving 33 rank configurations and 46,230 inequalities. A separate SLSQP optimization tests 18 instances through dimension five and reports a maximum coordinate difference below \(2\times10^{-15}\). Weight computations compare rank-deficiency scale, variance and mean geometric squared distance through dimension one million.

Finite computation does not establish the all-dimensional theorem or the central limit theorem; these follow from symmetry, strict convexity and saddle-point analysis. No independent mathematical audit has been performed.
