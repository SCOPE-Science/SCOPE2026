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
# Reproduction
Run `python verify.py` using only Python 3 standard-library modules. The exact-rational test returns `VERIFY_OK exact_rational_patterns=10 means=10 winning_probabilities=10 direct_time_probabilities=50`. It validates finite first-hit probabilities both from rational PGF coefficients and direct rational circle-orbit midpoint iteration, and separately computes exact absorbing Markov chain expectations and right-hole probabilities. The analytic uniform claim, Markov entropy, and Hausdorff dimension are proved in `RESULT.md`; this finite checker cannot independently certify them. No independent audit was performed.
