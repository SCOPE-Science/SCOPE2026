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

# Reproducibility and verification limits

Run the included `check_heat_maximal.py` with Python 3 and no third-party dependencies. It tests the exact positive integer witness, an exact two-site identity, an analytic coordinate-supremum evaluator on 20,000 deterministic random pairs, a grid of 20,402 generalized-derivative configurations, and an independent 5,001-point time-grid evaluator on 250 vectors.

Actual run status: all assertions passed. Finite tests do not prove the global inequality; the proof relies on a complete envelope-Jacobian bound for every active parameter, followed by the standard weak-derivative-to-global-Lipschitz step. The supremum can be approached only as time tends to infinity. No independent mathematical audit has been performed.
