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

# Reproduction and limits

Run `python check.py` using standard Python. The script uses a two-variable polynomial ring with exact rational coefficients to reconstruct the proposed eight state weights and the stationary master equations of the independently defined continuous-time generator. It verifies normalization, all eight zero-balance identities, each mean and covariance formula, and exact derivative numerator identities. It then independently constructs and solves stationary linear systems by rational Gauss–Jordan elimination at 20 parameter pairs with both zero and strictly positive exchange rates. On execution, every assertion passed.

Because the generator identities hold as polynomial identities, they prove the stationary distribution for every parameter in the stated domain; positive weights and irreducibility give uniqueness. Sign and strict monotonicity conclusions follow from explicitly positive factors and do not depend on empirical sampling. No numerical evidence is presented as a proof of any infinite-domain or thermodynamic-limit assertion. No independent external review has occurred.
