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

The calculations in `tools/check_identities.py` symbolically verify the exact vector-field flux derivative and equilibrium identities with independent SymPy expressions, and output `VERTICAL_HOPF_FLUX_COVARIANCE_SYMBOLIC_OK` on success. They do not replace the stationary generator argument, the compact-support justification, or the rigidity proof, which appear in RESULT.md.

All observable averages refer to invariant probability measures in the original physical-time vector field. Invariance gives zero generator integral because the support is compact and stays strictly inside the positive octant. The theorem holds for any positive rate values; its non-vacuous periodic-orbit application uses the cited vertical-Hopf condition. Strict covariance statements are not extended to boundary-supported measures or unbounded nonstationary trajectories. Independent audit has not been performed.
