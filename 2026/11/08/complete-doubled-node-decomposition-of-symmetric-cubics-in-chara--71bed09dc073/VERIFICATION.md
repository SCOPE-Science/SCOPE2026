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

The attached `check.py` runs using only Python 3 standard library modules and no external data. It enumerates each binary point in dimensions 4, 8, and 12 and checks all gradient equations, point counts, the block restrictions of the gradients, Hessian rank, and the quadratic value on the polar radical. Expected terminal marker: `ALL_EXACT_FINITE_CHECKS_PASS`. The exact identities in the proof, rather than the finite experiments, certify the claims for all positive multiples of four and all algebraically closed characteristic-two fields. No independent audit or external certification was performed.
