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

The analytic sign proof in `RESULT.md` establishes uniqueness for all positive parameters and boundary cases. Supplementary `check.py` uses symbolic differentiation and numerical quadrature/optimization, as described in `RESULT.md`; it can be rerun under a Python environment with SymPy and SciPy. Numerical checks cannot replace the monotonic-ratio proof. There is no independent external audit or field validation.
