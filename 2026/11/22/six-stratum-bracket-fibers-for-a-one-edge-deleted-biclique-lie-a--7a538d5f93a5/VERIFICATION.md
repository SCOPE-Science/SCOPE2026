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

A complete scientific proof is in RESULT.md. The matrix product fiber calculation uses the independent cases rank \(U=0,1,2\); the one-missing-entry completion calculation treats ranks of the specified \(2\times2\) corner, with exceptional singular locus explicitly separated. All finite field characteristics are covered by the proof.

Run `python verification/finite_field_check.py` from the unpacked artifact. It exhausts all ordered vertex-coordinate pairs over \(\mathbb F_2\) and \(\mathbb F_3\), enumerates every target, and compares against the exact formula and unavailable-image size. Recorded authentic output is in `verification/check_output.txt`. Finite checks alone are not evidence for all extension fields. Source comparison and uncertainty are discussed in REVIEW.md and AUDIT.json.
