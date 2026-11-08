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

The standalone `verify.py` was executed with Python 3 using only standard-library exact rational arithmetic.

Observed output: `EXACT_VERIFICATION_OK 51 algebraic/matrix/threshold checks`.

The code checks exact polynomial and derivative identities, a sum-of-squares lower bound, the rational evaluation at the extremal test point, a uniform-hub eigenvector identity, 21 exact rational matrix inversions with arbitrary extra edges among neighbors, and the 28/29 dimension witness. Each matrix identity is checked against the rational operator assembled directly from its two resolvent matrices. The all-network, all-timestep statement and uniqueness of the two root crossings are proved symbolically in `RESULT.md`, not inferred from finite tests.

The numerical value of the unique scalar minimum is illustrative. No independent mathematical audit has been performed.
