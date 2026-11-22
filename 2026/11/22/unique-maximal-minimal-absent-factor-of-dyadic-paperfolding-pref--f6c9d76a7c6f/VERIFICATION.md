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

Run `python3 verify.py` with a standard Python 3 interpreter; no external packages or downloaded data are needed. The script independently evaluates the odd-part-mod-four sequence definition; compares the two possible eight-bit patterns in all sixteen residue classes; checks the four-block differences and every length-quarter factor; and reconstructs the exact maximal minimal-absent deck for all dyadic lengths from \(2^5\) through \(2^{11}\). It also performs a more extensive absence scan at the smallest three lengths.

Observed output: `VERIFY_OK base_patterns=32 dyadic_k=5..11 longest_absence_checks=7`.

The theorem for all \(k\ge5\) depends on the synchronization induction and two-occurrence argument in `RESULT.md`, not on finite enumeration. The verifier does not certify independent scientific review.
