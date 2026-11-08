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

Run `python checker.py` from the extracted file directory with Python and SciPy installed. It should print `PASS: 248 kernel-integral, mixed-moment, variance, and sharp-correlation checks`. These checks independently integrate the killed Green kernel and compare the resulting moments and correlations with the closed-form formulas.

The exact Green kernel was checked analytically by its differential equation, boundary behavior and jump condition. The mixed moment and finiteness boundary use Tonelli and strong Markov arguments, which are not established by finite numerical checking. The full bivariate law, non-positive functional exponents and finite-interval cases are not proved.
