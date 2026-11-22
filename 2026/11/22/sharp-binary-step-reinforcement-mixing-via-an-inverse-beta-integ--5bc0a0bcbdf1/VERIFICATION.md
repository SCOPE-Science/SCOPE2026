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

The independent rational recursion `check.py` reproduced 683 exact assertions comparing a direct count Markov chain to coefficients of the coupled formal ODE, and separately computed asymptotic diagnostics at fixed positive copy probabilities. These finite checks are diagnostic only: the proof of the dominant-pole asymptotics is analytic, in `RESULT.md`.

For reproduction: `python check.py` (Python 3 standard library). All source needed for the checker is embedded alongside this file. Independent mathematical assessment has not been performed.
