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

The complete population/detection model, Fisher matrix and proof appear in RESULT.md. Execute `python checker.py` with Python 3 and no external dependencies. The packaged diagnostic checker passed **1258 assertions**: Gaussian moment recurrences, finite differences of the Gram derivative, strict diagnostic-grid elasticity decreases, five numerical scalar optima, and objective comparisons. Proof of strict global monotonicity uses the jointly concave rescaled derivative kernel and the Prékopa marginal theorem; finite sampling of parameter space is not treated as exhaustive. The formula for the lower bound is approximate to shown precision. The referenced older primary paper was not fully accessible, so literature priority is provisional. No external validation or independent audit is asserted.
