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

Run `python3 verify.py` from the extracted artifact directory. On a checked run it printed `VERIFY_OK canonical=292824 independent_split_crosschecks=400` and the exact size distributions by one through four intermediate values. The verifier independently checks representatives of each permitted minimal-failure size with direct red/blue partition enumeration.

The main theorem requires both the mathematical normal-form reduction (which removes unbounded intermediate alphabet size) and the complete finite state census. Direct random split checks alone cannot establish the theorem. The computation exhaustively enumerates sorted tuples of the 49 possible mixed three-input Boolean-output fibre states, with 49, 1225, 20825 and 270725 configurations for one through four fibres. Each minimal-failure candidate is checked against every possible input selection and all one-row deletions. The enumeration is exact and uses only Python's standard library; independent formal or peer validation has not been performed.
