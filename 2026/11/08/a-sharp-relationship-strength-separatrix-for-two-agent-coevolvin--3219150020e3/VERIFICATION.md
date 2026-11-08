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

Run `python verify.py` using Python 3 and installed NumPy and SciPy. It directly tests the differential conservation law over 180 parameter points, verifies first-integral conservation at 36 state/time samples under independent ODE integration, and checks the predicted limiting states in three subcritical, two supercritical and one critical examples. The program also solves the polarized limiting equation independently with a scalar root finder. The current version prints the count of all 222 assertions when successful.

The exact proof is supplied in `RESULT.md`. The code is finite numerical evidence, not an exhaustive search or a proof of the all-parameter theorem. Near the transition the tie strength is extremely small, so floating-point results require care; the verifier checks only finite times and loose asymptotic tolerances at the critical point. The analysis has not been independently audited.
