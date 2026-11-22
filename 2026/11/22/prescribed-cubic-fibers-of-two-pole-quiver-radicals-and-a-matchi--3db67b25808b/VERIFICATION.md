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

Run `python3 check.py` from the directory containing the supplied files. It requires only Python 3 and prints the recorded `checker_output.txt` when successful.

The first check exhausts all arrow variables in eleven finite-field/graph configurations, enumerates the exact target-support histogram, and compares each fiber with the independently evaluated subset formula. It also verifies the matching–independence identity and the leading coefficient of the zero-fiber polynomial. The second check builds the complete positive-length path basis and directly multiplies all elements of three small quiver radicals, thereby checking that higher path coefficients do not alter the prescribed cubes.

These finite tests establish the listed cases, not the theorem over all fields and graphs. The complete mathematical proof is in `RESULT.md`. No external independent audit has been performed.
