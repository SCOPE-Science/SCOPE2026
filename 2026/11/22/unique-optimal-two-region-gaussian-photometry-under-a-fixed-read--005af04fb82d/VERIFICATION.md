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

The claim is proved analytically in `RESULT.md`, with exact Poisson Fisher reduction, a strict symmetric-decreasing rearrangement equality argument, a unique-zero derivative proof, and two asymptotic arguments. The standalone `CHECK.py` supplies additional finite numerical and matrix-identity diagnostics; finite tests do not certify the continuous or infinite parts of the claim.

Run `python CHECK.py` in the directory containing the packaged files. Executing the standalone checker in its authored directory produced `PASS 24844 deterministic diagnostics; analytic statements are proved in RESULT.md`. A separate replay from the extracted delivered package checks that the embedded bytes reproduce this output. The Fisher design is explicitly a local limit at vanishing source flux, with both means positive because the sky background is positive. No experimental or independent validation has been performed.
