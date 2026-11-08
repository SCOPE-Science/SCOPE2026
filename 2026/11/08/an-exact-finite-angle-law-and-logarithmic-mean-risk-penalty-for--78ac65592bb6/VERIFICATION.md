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

**Mathematical proof:** RESULT.md gives the complete triangularized pencil, the nullspace/projective Gaussian ratio argument, the independent-exponential ratio law, the exact CDF and two evaluated moment integrals. The asymptotic claims are deductions from the displayed exact formulas, not from simulations.

**Reproduction:** With Python 3 and NumPy, run `python verify.py` in this directory. The script constructs independent complex Gaussian matrices, forms the actual reduced Petrov–Galerkin matrix with exact arithmetic identities checked numerically, compares selected-branch Rayleigh quotients against five exact CDF values for three distinct angles, checks 768-node Gauss–Legendre quadrature against each closed moment formula, and checks small-angle normalization sequences.

**Limits:** Floating-point tests are approximate checks at specified angles, not rigorous error bounds for an infinite family. Unconditional moment rates are proved symbolically. Selection by a general software eigensolver and numerical singularities are outside the scope. No independent mathematical audit has been performed.
