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

A standalone finite checker `verify.py` uses only the Python standard library. Invocation: `python3 verify.py`. It exhaustively compares direct ballot-level JR and score-maximization tests against the analytic occupancy formula in ten small parameter cells, totaling 374,592 profiles. It also checks three non-half Bernoulli probabilities by independently summing individual profile weights with exact rational arithmetic. All checks passed.

The exact general formula and asymptotics require the combinatorial proof in `RESULT.md`; finite enumeration is not treated as a proof. No independent scientific audit has been performed.
