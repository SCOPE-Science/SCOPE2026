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

# Verification and scope

The proof is symbolic over every odd-characteristic finite field. The included standalone `verify_adjoint.py` separately reconstructs the linear transformations from the basis Hopf operations and exhaustively checks ranks over four prime fields, printing `SWEEDLER_HOPF_ADJOINT_RANKS_OK` on successful completion. No external libraries are needed. These finite checks corroborate but cannot replace the all-field proof. The representation kernel, image quotient, and rank-three gap are proved algebraically. No independent audit or external certification has been performed.
