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

# Reproduction and verification

Run `python check.py` with Python 3 and no third-party packages from this directory. The checker uses `fractions.Fraction` to compare exact quadratic Jury inequalities over finite grids of slopes, cohort fractions, and Ricker parameters, independently checks the stability-window formulas, verifies the unique extremal fraction, and computes exact matrix powers through step 60. It also uses floating-point eigenvalues as subsidiary checks where the strict boundary is separated from zero. The actual run produced `PASS: 3554 assertions`.

The all-parameter stability statements are proved algebraically in `RESULT.md`; the finite grid does not prove them by enumeration. The nilpotent matrix calculation yields the boundary power law for all integer times analytically, and the checker verifies particular cases. Nothing here verifies nonlinear stability at a nonhyperbolic boundary, global persistence, or external historical priority.
