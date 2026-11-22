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

# Verification scope

The `verify.py` script in this package, with `requirements.txt`, was executed to produce `verification_output.txt`. It checks independent quadratures of the underlying Gaussian arcsine kernel, both covariance-normal equations, finite-pair projection identities, the exact radical trisection case, the critical-equation root and the reported numerical constants. All 1,359 numerical assertions passed in the recorded execution.

The continuum sign identity, moment integral, decoder uniqueness, and symmetric-class optimizer uniqueness are established in `RESULT.md` by analytic arguments; finite numerical checks are not proofs of these infinite-domain statements. The optimization over nonsymmetric time pairs and the priority of every equivalent earlier formulation have not been independently settled.
