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

# Reproducible checks

From the package directory run `python grassmann_check.py` with Python 3 and NumPy. The expected final line is `GRASSMANN_RANK_THREE_NEGATIVE_TYPE_CHECKS_PASS`.

The checker enumerates all binary 3-dimensional subspaces in ambient dimension six, builds two independent incidence matrices by actual subspace containment, and checks exact integer polynomial identities and traces for their Gram matrices. Those identities imply incidence eigenvalues with the stated multiplicities, independently of the presentation of the theorem. The threshold root is checked numerically for field orders \(2,3,4,5\) and ambient dimensions \(6,7,8,10,15\), with endpoints and strict location asserted.

The integer identities are exact finite verifications; the floating-point roots are crosschecks only. Neither computation proves the universal eigenvalue identity or the large-dimension asymptotic. Those follow from the supplied harmonic-chain source and the parameter-uniform inequalities in `RESULT.md`. No independent mathematical audit has been performed.
