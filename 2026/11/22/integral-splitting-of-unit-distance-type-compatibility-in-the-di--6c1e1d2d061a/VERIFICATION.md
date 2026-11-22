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
# Verification and reproducibility

The proof's key exact computations are the displayed inverse of the one-coordinate compatibility matrix \(T\), the three integer zero pairings with the exceptional row vector, and the resulting exact identity \(HD^{-1}H^{\mathsf T}=0\). These imply the full all-size integer congruence; no uncomputed enumeration or external certificate is used to establish the infinite statement.

From the directory containing this file, run `python VERIFY.py` using Python 3 standard library. The checker reconstructs finite metric types without relying on the theoretical classification, computes all unit-compatibility entries for parameter sizes one through four, checks the tensor and exceptional block identities and Schur cancellation with exact integers, and calculates ranks over three prime fields. Expected last line: `VERIFY_OK`.

The finite examples are not an exhaustive test of all parameter sizes; the universal proof in `RESULT.md` supplies that step. The code does not verify research priority or any broader claim involving nonequilateral bases or different mutual distances.
