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

# Verification notes

Run the included standalone script with `python verify.py`. It uses only the Python standard library, computes exact rational transition probabilities, checks the two-step worst-start identity and the differentiation numerator through elementary bivariate polynomial operations, and examines the sign regions for 4,406 finite parameter cases. It also prints three rare-corruption numerical diagnostics and an exact rational example.

The all-parameter proof is in `RESULT.md`: every starting level is considered, the cubic's derivative sign is controlled on its full domain, and the asymptotic follows by a direct root sandwich. Finite enumerations are not an exhaustive substitute. No external audit or independent validation has been performed.
