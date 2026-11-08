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

The formulas in `RESULT.md` follow by symbolic differentiation, two-node mode decomposition, symmetry reduction, analytic implicit-function arguments, and a one-dimensional center-manifold sign calculation. `CHECK.py` executes exact-rational checks of all stated coefficients and eigenvalue identities. A reproducible command is `python CHECK.py` (Python 3, SymPy required). Numerical checks, if any, illustrate but do not establish the theorem. The theorem is local and proves no global convergence or stochastic claim.
