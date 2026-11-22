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

# Verification scope

For the theorem in `RESULT.md`, the proof is independent of the computation. The exact kernel expansion and reciprocal recurrence are derived symbolically. The sharp threshold follows from the sign of the characteristic discriminant, including the repeated-root case; failure follows from a real trigonometric oscillation, not an eventual-negativity heuristic. The exact first-negative index and its inverse-square-root scaling are likewise proved for every fixed admissible \(a>1\).

Run `python verify_two_defect.py` with Python 3 (standard library only). The script checks 108 rational parameter pairs and twelve numerical near-critical scenarios and reports `TWO_DEFECT_EXACT_CHECK_OK 120`. The 108 coefficient tests inspect 200 initial coefficients each; the script does not claim that this bound detects every non-Pick parameter. Near-boundary scenarios test the explicit sign-index formula and compare the scaling coefficient with the claimed limit. No finite enumeration constitutes a proof of the infinite assertions. An independent audit has not been performed.
