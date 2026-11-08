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

# Verification record

`python verify.py` (requires SymPy 1.13 or newer) completed successfully. The checker reconstructs the four-state generator from the stated jump rates, forms its four principal cofactors, and tests exact symbolic identities for the stationary normalization, directed-current numerator, full even-current factorization and quadratic response. It uses an **independent standard-library rational Gaussian-elimination solver** for the stationary balance equations on 288 exact-rational positive-parameter/bias instances. The chosen half-bias inversion example is checked exactly, including opposite signs on both sides.

These finite checks are supplementary: the all-parameter proof is a cofactor identity plus positivity from the finite-state matrix-tree theorem. The tests do not demonstrate uniqueness in the literature, nonlinear dynamics, large-system behavior or a separately performed external audit.
