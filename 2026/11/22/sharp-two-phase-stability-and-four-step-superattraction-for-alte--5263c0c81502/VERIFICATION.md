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
The analytic proof in `RESULT.md` gives every quantifier and restriction. `check.py` uses Python's exact `fractions.Fraction` arithmetic to validate the rational trace and determinant expressions and the nilpotence and nonzero-matrix identities. It also runs a numerical nonlinear sanity check, which is **not** a substitute for Taylor's theorem and does not establish any global nonlinear convergence.

A run of `python3 check.py` produced `DEADBEAT_EXACT`, `TWO_PHASE_FORMULAS_EXACT`, `JURY_IDENTITIES_EXACT`, `QUARTIC_FOUR_STEP` sample lines and `CHECKS_OK`. No external or independent review was performed. Boundary dynamics for general \(C^3\) objectives, extensions to more directions or dimensions, and historical priority outside the inspected sources remain unproved.
