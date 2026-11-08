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

The algebraic proof is provided in RESULT.md, including the complete integer-potential dichotomy and the disjoint real-volume decomposition. The executable `artifacts/verify.py` separately enumerates small rooted lattice point sets, reconstructs Eulerian numerators, and calculates several weighted convex hull volumes from halfspace inequalities.

Command: `python artifacts/verify.py` (requires Python 3; numerical volume checks require NumPy and SciPy).

Completed output: `MATCHING_LIPSCHITZ_EHRHART_CHECKS_PASSED integer_profiles=34 hstar_profiles=6 independent_hulls=8`.

Limits: 34 finite integer checks and eight numerical-volume instances are not infinite proofs. The independence of the closed-form analytic argument from the finite checks is essential. Numerical hull volumes use finite tolerance. No independent audit or other external verification has been conducted.
