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

Run `python3 verify_involution_fixedset.py` in a directory containing the attached script. The exact rational test enumerates every fixed-point set of feasible parity and every matching of its complement for each order from 2 through 12. It compares the conditional inversion average with the theoretical expression and checks the sharp endpoints and extremizer characterizations. Recorded execution: PASS; 20,414 assertions and 189,078 enumerated involutions across conditioned sets.

The finite test does not certify the identity for unbounded order; the complete matching argument in RESULT.md supplies the proof. There was no independent external audit.
