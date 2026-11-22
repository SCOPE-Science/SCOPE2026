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

All calculations in `verify.py` use Python's built-in `fractions.Fraction`, exact binomial coefficients, and exhaustive permutations. The self-check currently reports `PASS: 1286 exact identities, inequalities, and exhaustive checks`. The proof in `RESULT.md`, rather than finite enumeration, supports the statements for every integer window width and rank.

Verified identities: beta-polynomial CDF integration for the full-width lag; exact lag-one joint retention and covariance; strict sign conditions; exact central null criterion; optimal discrete ranks; exhaustive permutation comparisons at small widths. Unproved limits: intermediate lag covariances, joint independence beyond pairs, atom-containing or dependent inputs. Independent audit: not performed.
