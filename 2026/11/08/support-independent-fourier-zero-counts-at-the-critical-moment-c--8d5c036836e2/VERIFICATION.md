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

The complete proof is in `RESULT.md`. The exact cyclotomic reduction, Lagrange evaluation-hyperplane identity and diagonal orbit transversality prove the count for every allowed prime and integer support size. `CHECK.py` is a standalone Python 3 standard-library verifier with direct enumeration of polynomial coefficients, an independently structured hyperplane count, and three lower-degree counterexamples. It prints `CHECK_OK prime_instances=6 hyperplane_instances=4 lower_degree_counts=141,51,231 B4=1,34,72,24` on success. Finite checks are supporting tests and do not substitute for the full algebraic proof. No independent audit has been performed.
