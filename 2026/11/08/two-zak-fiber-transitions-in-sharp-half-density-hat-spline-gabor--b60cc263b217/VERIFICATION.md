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

# Mathematical verification and limits

The analytic proof reduces frame bounds to scalar Zak-fiber extrema, computes two exact Laurent polynomials, proves simultaneous phase minimization/maximization by coefficient dominance, and solves the remaining piecewise quadratic problem. The endpoint and switching equations are stated in the proof. The standalone `verify.py` uses only Python standard-library operations and reports `HAT_SPLINE_EXACT_BOUNDS_CHECKS_PASS 20242`, including rational coefficient-dominance checks, direct finite Zak sums, and global mesh inequalities. Tests are finite; the mathematical proof, not numerical verification, establishes the all-real theorem. No independent mathematical audit has been performed.
