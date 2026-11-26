---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and mathematical limits

`python3 check.py` uses Python's standard library to reconstruct the two carry states and their output digit probabilities as exact rational numbers. It checks stationarity, the frequency vector computed from the stationary carry law, and one-position digit marginals through eight positions by comparison with integer prefix counts.

The almost-sure frequency statement is proved in `RESULT.md` using the Markov ergodic theorem and the bounded martingale-difference law. Finite marginal tests alone do not establish it.
