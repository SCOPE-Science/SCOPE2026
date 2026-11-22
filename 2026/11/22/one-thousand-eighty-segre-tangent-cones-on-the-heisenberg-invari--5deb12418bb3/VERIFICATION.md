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

The exact symbolic checker `VERIFY.py` was run with Python and SymPy, and all its assertions completed. It verifies the defining equations, point, rank of the linear part, three quadratic determinantal initial forms, representative Segre Jacobian rank, and Hilbert-function identity.

The infinite/global argument additionally uses two mathematical facts rather than computational extrapolation: primality of the maximal-minor ideal and the equality-of-dimensions argument for the full associated graded local ring; and transitivity of the normalizer on the singular points, using the explicit symmetry and set-theoretic classification from arXiv:2611.16593v1. These deductions are set out in `RESULT.md`.

Limits: no finite symbolic check proves the global orbit assertion by itself, and no independent audit, completed formal-analytic classification, or complete verification of inaccessible older historical literature is claimed.
