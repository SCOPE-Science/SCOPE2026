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

# Verification record

The exact verifier is `verify.py`, with its full 139-row expected finite census in `profile_certificate.csv`. Run `python3 verify.py` from the directory containing these files. No third-party dependencies are required. The actual output in `verification_output.txt` verifies the complete partition spectrum through size ten, independent rational-series coefficients, and direct tuple-label enumeration for the two ten-point witnesses.

The checker evaluates a finite list of instances of the persistent family. Its universal validity rests on the explicit symbolic expressions and cancellation in RESULT.md; the finite spot checks alone do not prove the all-size statement. The cited mathematical literature was compared for historical context, and independent auditing has not been conducted.
