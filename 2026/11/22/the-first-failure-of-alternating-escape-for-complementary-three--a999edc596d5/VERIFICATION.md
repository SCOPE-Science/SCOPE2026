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

Run `python verify.py` with a standard Python 3 interpreter in the same directory. No packages or external files are required. The checker performs independent binary-word enumeration, exact transfer recurrence checks for every one of the 510 schedules of lengths one through eight, complete first-reversal minimizer enumeration through length five, exact determinant interpolation for both period matrices, rational sign checks, and strict rational power inequality. It returned `PASS: complete finite tests and exact spectral certificates`.

The verifier does not establish anything about global optimization among all infinite schedules, and finite enumeration cannot by itself justify the spectral limits. Those follow from the explicit primitive nonnegative matrices and Perron–Frobenius theory in RESULT.md. The published priority comparison has residual limits listed in REVIEW.md.
