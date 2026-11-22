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

# Reproduction and limitations

Run `python check_parabolic_diameter.py` with a Python environment containing NumPy and SciPy. It verifies the exact algebraic transition numerically, samples candidate diameters, and evaluates two independent fixed-width near-diameter integrals, printing `PARABOLIC_DIAMETER_GOLDEN_TRANSITION_CHECKS_OK`. Numerical agreement is supplementary; it does not replace the global stationary-point proof and local asymptotic area integrations in RESULT.md. The analytic proof establishes fixed-parameter limits, not uniformity in the parameter across the critical transition.

This package has not undergone independent mathematical audit or independent validation.
