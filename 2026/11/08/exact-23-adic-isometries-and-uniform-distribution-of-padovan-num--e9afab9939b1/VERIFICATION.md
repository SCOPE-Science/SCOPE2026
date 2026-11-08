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

## Reproduction

Run `python verify.py` with Python 3 and no third-party dependencies. The verifier constructs the companion matrix independently, checks its 22-step and 506-step reductions modulo 23 and 529, checks all 22 slopes, and enumerates complete recurrence periods for the first three prime powers. It also checks 2000 seeded comparisons with exact modular valuations. All these are finite corroborations; the general theorem depends on the stated prime-power matrix lifting lemma and the congruence certificates.

## Limits

Only the classical Padovan normalization and the prime 23 are covered. No independent audit has been performed.
