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

# Verification and reproducibility

The proof is contained in `RESULT.md` and is logically independent of the finite script. Run `python3 verification.py` using the Python 3 standard library in a directory containing this file. The script was executed successfully and reported `PASS: 391 independent finite/exact checks; no universal claim inferred from sampling.`

Exact checks include the rational period-four cycle and four-step multiplier at \(m=2\), \(b=5/2\), and the formal cubic coefficient of the normalized critical second iterate for nine integer exponents. Numerical checks verify the exchange equations and multiplier formulas for seven positive exponents (including nonintegers) and six positive hyperbolic parameters each, the four-step coordinate identity on representative positive samples, and the signed critical \(n^{-1/2}\) relaxation in four representative exponents.

Finite tests do not prove uniqueness, global attractivity, convergence for all initial states, invariant probability classification, or the asymptotic coefficient for all real \(m>1\); these are established by the analytic arguments in `RESULT.md`. No independent audit was performed.
