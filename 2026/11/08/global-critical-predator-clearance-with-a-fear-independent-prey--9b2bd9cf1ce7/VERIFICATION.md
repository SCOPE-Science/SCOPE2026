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

The proof is self-contained in `RESULT.md`. The packaged `verify.py` runs exact rational symbolic checks of the critical condition and coefficient evaluations, then non-certifying finite-time ODE diagnostics at two positive fear strengths. Run from the extracted package with `python verify.py`; dependencies are Python 3, SymPy and SciPy. A successful replay prints `VERIFY_OK`.

The infinite-time global convergence and asymptotic claims are justified by the mathematical proof, not by the finite-time solver. The diagnostics are restricted to initial state \((0.8,0.2,0.1)\) and do not explore every physical initial condition. A rigorous parameter-wide convergence claim cannot be inferred from a finite numerical experiment; no such inference is used.
