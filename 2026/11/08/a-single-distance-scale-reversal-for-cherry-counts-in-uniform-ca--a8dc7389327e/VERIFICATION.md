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

The bundled `check_cherry_distance.py` was run with Python 3 and passed. It exhaustively constructs all Prüfer codes at sizes four through seven and independently measures leaf siblings and unordered pair distances, checking the covariance against the analytic expression with exact fractions. It additionally evaluates 197 finite orders for shell sums, one-switch signs, and Wiener negativity, using exact rational arithmetic.

These checks corroborate, but do not prove, the infinite-order shell classification. The proof is in RESULT.md: forest extension and cherry-marking identities give the exact covariance; strict log concavity supplies the global sign theorem. Only a self-review was performed.
