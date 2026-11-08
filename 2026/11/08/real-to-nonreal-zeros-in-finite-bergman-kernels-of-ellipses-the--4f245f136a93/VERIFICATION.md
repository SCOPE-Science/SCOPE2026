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

# Reproducibility

Run `python check.py` in an environment with Python 3 and SymPy. The script verifies exact symbolic identities: normalized degree-four rational formula, discriminant, reciprocal quartic, Newton deficit, degree-two boundary, and eight thin-limit Chebyshev cases. Its success string is `ELLIPSE_FINITE_KERNEL_PASS`.

The all-degree existence assertions are analytically proved in `RESULT.md` by coefficient convergence, simple-root stability, and strict Newton inequalities; finite symbolic tests do not certify infinitely many indices. This file contains no independent validation.
