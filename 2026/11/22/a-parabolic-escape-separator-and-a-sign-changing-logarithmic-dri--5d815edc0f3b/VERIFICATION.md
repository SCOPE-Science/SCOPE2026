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

The proof is analytic. Reproduction: run `python verify.py` with Python 3.10+; only the standard library is used. The program checks exact rational coefficient cancellation for several rational parameters and performs finite shooting diagnostics near critical orbits. Finite tests are non-exhaustive and cannot prove the global existence, uniqueness, or asymptotic results; those are established (except uniqueness, which is not claimed) by the monotone shooting, Riemann-sum and summable-error arguments in RESULT.md. No external independent assessment has been undertaken.
