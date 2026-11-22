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

The core proof uses the exact stationary conditional-moment equation, a real symmetric spectral transform valid under detailed balance, and a Rolle-induction zero bound for reciprocal-power kernel combinations. The specified `checker.py` uses Python standard-library rational arithmetic to independently compute the three-state determinant and Cramer numerators, differentiate them and verify 38 exact balance systems; it also evaluates the unique positive root and exact slow/fast limits. Run `python3 checker.py` in a directory containing this package.

The calculation is finite only for the explicit example; the \(n-2\) theorem follows from the universal proof in RESULT.md. Checking numerical examples cannot certify literature novelty, physical calibration, stochastic sample-path extremes or nonreversible dynamics. No independent scientific audit has been conducted.
