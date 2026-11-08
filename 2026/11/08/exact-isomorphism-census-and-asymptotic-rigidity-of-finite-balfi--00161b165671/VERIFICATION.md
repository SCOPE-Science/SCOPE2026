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

# Reproducibility and limits

Execute `python3 verify_balfi.py` in the same directory. It uses the standard library only, computes exact integers, directly enumerates all BALFI tables for atom counts one and two, and checks the Burnside isomorphism counts for atom counts through five. Success is the final line `BALFI_VERIFY_OK`.

The checker directly applies both equations for each table entry. It does not use stored enumeration files or numerical approximation. The exact formulas and asymptotic estimate are proved for all positive atom counts in `RESULT.md`; the finite computations are corroboration and not a substitute for the uniform argument.

There is no independent audit or external formal certification of this result.
