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

# Verification notes

The standalone `CHECK.py` was executed with standard Python and completed 343 assertions without error. It independently compared all ordered parent-choice configurations with the derived leaf Markov chain for small sizes and three integer exponents, checked exact expectations and variances, compared two classical endpoint laws, and confirmed numerical limits for multiple positive exponents. The tests are finite and do not establish the almost-sure law or functional central limit theorem; those require the recurrence, martingale inequalities, quadratic-variation convergence and integral-equation arguments in `RESULT.md`.

No independent mathematical audit has been performed. Historical-priority assessment remains provisional because the closest 2026 paper's full manuscript could not be inspected through accessible sources.
