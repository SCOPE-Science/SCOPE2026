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

## Reproducibility
Run `python3 check.py` with the Python standard library. The script computes exact rational finite-step joint laws for four parameter pairs and compares their moments to independent recurrence calculations. It then tests the analytic bulk limits against finite-size recurrences with 10,000 steps.

The packaged program reported **PASS: 952 deterministic assertions** when executed. Its computations are finite; the proof of weak convergence, beta density, heading calibration, and asymptotic gamma ratio appears in RESULT.md and does not depend on numerical extrapolation.

## Scope of verification
No formal proof assistant or third-party certification was used. The stationary beta density and its transport equations already appear in the cited active-particle literature; the claim assessed here concerns the scaling limit of the ageing walk and related observable consequences. No independent scientific audit has been performed.
