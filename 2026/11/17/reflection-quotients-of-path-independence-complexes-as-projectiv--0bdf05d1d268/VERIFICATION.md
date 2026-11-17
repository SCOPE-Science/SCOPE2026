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

Run `python3 verification/verify.py` from the directory containing this document. It uses only the Python standard library. The recorded standard output is embedded at `verification/verification_output.txt`.

The test enumerates every independent face for path sizes 2 through 24, verifies the simultaneous fold is a simplicial map contiguous to the identity, fixes its target and commutes with reversal for every independent face of sizes 6 through 24, and reconstructs Euler characteristics of the ambient and geometric fixed complexes from faces, comparing them with the predicted representation-sphere Euler characteristics and the orbit-space Burnside relation. All checks passed. The proof of all-integer homotopy types is the explicit equivariant retraction, base models and join decomposition in RESULT.md; the program is corroborative and is not an exhaustive verification beyond size 24.

No claim of independent mathematical validation is made.
