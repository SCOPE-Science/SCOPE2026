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

# Verification and reproducibility

The scientific result is reconstructed analytically in `RESULT.md`, including all endpoint assumptions and the strict monotonicity proof. Run `python verify_policy.py` using Python 3 and no third-party packages. The actual replay on the packaged checker passed 139 deterministic assertions: the normalized beta-shaped threshold density, detection function and derivative identities, inverse formula, low-overhead and long-overhead laws, and sampled comparisons with alternate durations.

Finite assertions do not prove strict concavity for every positive parameter or uniqueness over all exposures; those assertions rest on the symbolic derivative and endpoint arguments in the proof. No independent audit or external mathematical certification has been performed. This version has no empirically calibrated data and makes no finite-sample statistical claim.
