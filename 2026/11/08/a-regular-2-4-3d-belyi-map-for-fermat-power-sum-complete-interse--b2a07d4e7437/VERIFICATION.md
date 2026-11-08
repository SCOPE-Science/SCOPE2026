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
# Reproducibility checks

Execute `python3 verify.py` from this directory with SymPy available. The executed run printed `CERTIFICATE_OK: universal discriminant, symmetric identities, and passport checks`.

The exact script checks the discriminant of `T**4-E3*T+E4`, Newton's relation among elementary symmetric functions, the repeated-coordinate equation, the degree counts of the three branch divisors, and genus/ramification/fiber arithmetic for integral parameters 3 through 39 excluding 4. The script does not by itself prove that the indicated projective branch divisors are reduced, that no other branch points exist, that the complete intersection is smooth for every degree, or that its full automorphism group has the claimed order. Those universal arguments occur in RESULT.md, with the external full-automorphism theorem explicitly cited. No independent audit was performed.
