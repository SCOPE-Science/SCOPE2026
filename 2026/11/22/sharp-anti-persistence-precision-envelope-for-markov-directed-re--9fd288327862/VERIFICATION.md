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

# Reproducibility

Run `python verify.py` with Python 3 and no extra dependencies. The program checks the stationary two-state transition law, verifies finite-horizon moments by two algebraically distinct constructions, differentiates a tilted Markov-renewal kernel for a genuinely random-duration example, tests the sharp transition constraint, and checks the strict marginal-bound comparison.

The general claim is proved in `RESULT.md` using conditional variance, a bounded stopped-martingale argument, and the exact two-state stationarity constraints. The computation is a consistency check, not an infinite-horizon proof or independent scientific audit.

The comparison with the 2026 marginal reversal-information inequality is explicitly outside that inequality's i.i.d.-sign domain. Full dynamical entropy production for correlated orientations is not estimated here.
