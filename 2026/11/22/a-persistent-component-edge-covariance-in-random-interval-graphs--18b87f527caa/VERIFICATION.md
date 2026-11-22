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

The supplied `check.py` enumerates all uniform pairings of `2*n` ordered endpoints for integer `n` from 2 through 7 and computes component counts from empty cuts and edges from interval overlap. Exact `Fraction` arithmetic checks means, variances, and covariance against the independent finite-sum formulas. The largest exhaustive case enumerates 135135 perfect matchings. Checks at larger `n` evaluate exact rational formulas but are not asymptotic proofs.

Proof of the asymptotic covariance, component variance, rarity of disconnection, and correlation constant is contained in `RESULT.md`. No external software libraries or external certificates are needed; no independent mathematical audit has been performed.
