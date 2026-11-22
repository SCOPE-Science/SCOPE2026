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

# Reproducibility and limits

Run `python verify.py` with Python 3 and SymPy. The program verifies, over exact rational polynomial arithmetic, the three moment formulas, the rational objective and derivative, the one-dimensional polynomial isolating signs and the precise resultant. It independently tests irreducibility of both degree-six polynomials after reduction modulo the prime 113. Its high-precision printed approximations follow these exact checks.

The global maximizer argument also requires Descartes' rule of signs and the sign of the derivative denominator; those steps are written in `RESULT.md`, not inferred from the executable's finite numerical tests. The geometric inequality and asymptotic sharpness reduction are cited previously proved theorems; only their dimension-four algebraic specialization is claimed as new. Numerical root finding is used for presentation, not for the proof. No independent audit has been performed.
