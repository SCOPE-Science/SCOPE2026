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
# Verification

Run `python verify.py` with Python 3 and SymPy. The script reconstructs both log-density derivatives exactly, verifies the critical transformed negative-mode expansion, checks the exponential law coupling identity, and evaluates finite-model sanity checks over twelve parameter/sample-size cases. Analytic proofs of the infinite quantifiers, exponential extinction, stochastic-order limit and strict mode uniqueness are in RESULT.md; the finite test grid is not an infinite proof.

No independent mathematical audit was performed. The priority comparison is best-knowledge rather than exhaustive.
