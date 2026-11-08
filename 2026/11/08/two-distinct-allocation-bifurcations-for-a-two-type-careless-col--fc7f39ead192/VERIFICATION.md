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

# Reproducibility checks and limits

From the extracted package directory run `python3 verify_two_coupon.py` (Python standard library only). The checker builds each four-state post-erasure Markov transition matrix directly from the acquisition/erasure rule, solves an independent three-transient-state hitting system and a normalized four-state stationary linear system using exact rational Gaussian elimination, and compares both results to the closed forms at a family of rational input pairs including zero-loss boundaries. It checks derivative numerator monotonicity with exact rational arithmetic and the budget-one-half witness, plus finite-mesh optimization diagnostics for 199 budgets. An initial run passed 20,031 assertions and finite numerical diagnostics.

The symbolic derivative and endpoint polynomial argument in RESULT.md, not finite numerical tests, proves classification for every real budget. This package does not independently certify historical novelty, priority or correctness. Exact valid scope: two uniformly drawn labels, post-draw per-type independent erasure, and total loss strictly between zero and one. No external or independent audit has been performed.
