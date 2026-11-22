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

# Reproducible verification

The included `verify.py` was executed successfully with SymPy. Its exact-rational assertions separately check the quartic formulas, stationary resultant and subresultant, boundary witness, strict degree-12 Bernstein coefficients, Descartes three-interval root exhaustion, and all required whole-interval sign classifications. The reported optimizer coordinates are printed only after these exact checks.

Execute `python verify.py` with `sympy` installed, as specified in `requirements.txt`. No external data, downloaded papers or unprovided computational artifact is needed to reconstruct the finite symbolic checks.

Exact algebraic checks verify the individual explicit certificates; the written analytic proof explains why those certificates imply the global statement. No statistical simulation can establish absence of further stationary points. The literature comparison and publication priority have not received independent validation; no independent audit has been carried out.
