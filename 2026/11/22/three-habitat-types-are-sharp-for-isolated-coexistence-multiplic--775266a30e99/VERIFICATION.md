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

# Verification notes

Run `python verify.py` with Python 3 and SymPy. The script checks the stated rational rank-one kernels, exactly two positive roots of the reduced scalar equation, exact equilibrium equations, positive habitat vacancies, characteristic polynomials of the complete six-state Jacobians, and quartic Routh determinants. The general one-/two-habitat restriction is proved analytically in RESULT.md and is not inferred from finite enumeration. Robustness follows from nonvanishing exact Jacobian determinants. Numerical graphing is not needed. The proof and code make no claim about the stochastic finite-patch model, global attractors, or historical priority independent of the cited comparisons.
