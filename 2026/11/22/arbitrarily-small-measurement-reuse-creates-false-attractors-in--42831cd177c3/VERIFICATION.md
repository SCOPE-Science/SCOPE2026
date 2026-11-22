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

The exact rational checker was run from the current candidate files with Python 3 and returned `VERIFY_OK 2268`. It enumerates candidate signs and, in a subset of cases, all joint update-sign outcomes, checking all exact expectations and variances. The infinite-parameter claim, exact selection law, almost-sure wrong-limit bound, and full-refresh convergence are proved symbolically in `RESULT.md`, not inferred from finite sampling. No independent validation or external certification has occurred.
