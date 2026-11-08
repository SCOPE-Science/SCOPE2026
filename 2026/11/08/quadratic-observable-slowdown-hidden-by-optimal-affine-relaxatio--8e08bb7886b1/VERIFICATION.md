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

Run `python3 verify.py` in the directory containing the extracted files. The verifier uses the Python standard library only and, when executed for this record, passed 6,989 exact-rational and scalar spectral checks. It verifies exact conditional-branch stationarity of two Gaussian moments, the mixed first-moment operator, its trace and determinant, the repeated-root affine minimax tuning for perfect-fourth-power condition numbers, the exact covariance-error cubic, and its strictly negative and positive evaluations at the affine-rate and unit boundaries. The Gaussian stationarity, affine calibration, covariance strict-gap and realizable position-variance effect are established analytically in `RESULT.md`, not by exhaustive enumeration.

The checker never represents finite tests as proof of all dimensions. It neither certifies total-variation mixing nor checks practical conditional-Gaussian oracle cost. The older historical literature may contain a more general equivalent result; no independent audit is claimed.
