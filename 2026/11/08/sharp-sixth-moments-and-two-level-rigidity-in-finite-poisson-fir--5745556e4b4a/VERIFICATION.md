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

The supplied `check_poisson6.py` runs exact symbolic differentiation and exact rational central-moment calculations using a separate Bell recursion. It also tests attained endpoint witnesses in multiple dimensions and a bounded random sample of coefficient vectors. Its endpoint tests, bisection and numerical samples are finite diagnostics, not an infinite-dimensional or continuum certificate. The universal positivity and equality statements are proved by the analytical arguments in `RESULT.md`; no independent mathematical audit is claimed.

Reproduce with `python check_poisson6.py` using Python 3 and the SymPy library. The checker is deterministic.
