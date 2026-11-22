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

Run `python3 CHECK.py` for 54 deterministic comparisons between an independently discretized killed birth–death master equation and the closed first-binding joint probability-generating function, including multiple times, burst laws and generating-function arguments. Run `python3 TAIL_CHECK.py` for six positive-series comparisons near the three power-tail phases. Both require only standard Python 3.

The first checker uses a finite state cutoff and bounded time integration, while the second approximates finite or infinite positive sums. Neither is an infinite analytic certificate: the full proof of uniform early-age size bias, integrability and the Brownian heavy-tail asymptotics is in `RESULT.md`. All statements concern the model and hypotheses exactly stated there. No independent audit has been performed.
