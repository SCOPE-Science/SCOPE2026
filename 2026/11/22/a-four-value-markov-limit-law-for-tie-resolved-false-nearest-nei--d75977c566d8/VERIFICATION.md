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

The mathematical proof is in RESULT.md. The provided check.py uses rational arithmetic to test 81 interior transition parameter pairs for probability normalization, mean and variance; all passed. It also checks sixteen independently seeded sample paths of length 100000 for four Markov parameter pairs against their first-hit predictions; all deviations were below 0.012. Sampling is not a proof of the almost-sure statement, whose proof is the finite-state ergodic theorem together with the strong Markov property. The source's exact zero-distance FNN ratio convention was checked in its full HTML text. Independent validation was not performed.
