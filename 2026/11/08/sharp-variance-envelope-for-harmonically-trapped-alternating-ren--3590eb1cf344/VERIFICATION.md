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

Run `python3 verify.py` in the same extracted directory as this document. The checker reports `PASS: 468 independent assertions` and checks the formula against deterministic-cycle integration, exponential-flip Markov generator balance, Erlang-two Markov substage balance and exact rational instances. All unbounded-distribution claims are proved by renewal equations and convexity; sampled checks alone are not certificates for them. No independent validation was performed.
