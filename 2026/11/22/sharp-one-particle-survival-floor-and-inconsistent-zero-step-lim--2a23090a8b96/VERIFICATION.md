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

The theorem is proved symbolically by conditioning on the first Poisson predictor, applying the Poisson generating function to the binomial backtracking branch, and showing that state one cannot be revisited after an accepted death. The standard-library `verify.py` independently computes direct probabilities from truncated Poisson sums, checks the branch transition identities against the closed form, checks the first-order coefficient and finite-physical-time limit, and verifies the midpoint perfect-square minimum on a deterministic grid.

Run `python verify.py`. All finite numerical checks are supplementary: they do not prove equality at every parameter or the infinite-time limits. No independent mathematical audit or external numerical validation has been performed. The assumption that the propensity is zero for nonpositive population states must be retained to replay the specified process.
