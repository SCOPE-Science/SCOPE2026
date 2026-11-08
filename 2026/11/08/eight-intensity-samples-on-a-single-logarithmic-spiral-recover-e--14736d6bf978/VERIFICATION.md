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

The exact standalone checker `verify_spiral.py` constructs the eight Gaussian-integer nodes and the real Hermitian measurement matrix. On replay it checks rank eight, the eight-row kernel vector, the exact minor and Hermitian determinant, and the vanishing of each Hermitian evaluation. The abstract lower bound for seven samples and the analyticity argument for all open subarcs are established by proof, not by a finite test. No independent mathematical audit has been performed.
