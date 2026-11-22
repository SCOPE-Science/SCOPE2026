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

# Verification and limits

Execute `python3 verify.py` with SymPy installed. The script constructs the six-state weighted transition matrix from independent local deletion tests and compares its formal resolvent with the closed rational function by exact symbolic cancellation. It enumerates all admissible ternary words through length 13 and computes all unique valid one-deletion outputs directly. It checks transfer spectra, maxima, and extremizer counts through length 16, and the polynomial recurrence through length 26.

Observed checks: exact symbolic resolvent equality PASS; direct deletion spectrum through length 13 PASS; transfer/maximum/optimizer through length 16 PASS; polynomial recurrence through length 26 PASS. The all-length assertion is justified by the finite-state bijection and coefficient induction in RESULT.md, not by extrapolating the exhaustive range. No independent mathematical audit has been performed.
