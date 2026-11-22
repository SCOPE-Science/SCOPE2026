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

The equations, period-two axis and two-step block derivatives are checked by exact rational and symbolic algebra in `verify.py`. The script checks both Schur boundaries at the exact rational benchmark, the amplitude region classifications, and the structure of the quadratic axial drift. It prints a success summary only after every assertion passes.

The continuum-of-cycles statement is an exact consequence of \(hb=2\); the open-tube theorem is proved mathematically by a contracting equivalent norm and summable quadratic axial drift, not by simulation. Numerical eigenvalue examples are diagnostic only. Only axial cycles are classified, and the neutral/wall cases receive no additional nonlinear stability claim.

Run with Python 3 and `sympy` available: `python verify.py`. Independent mathematical validation has not been performed.
