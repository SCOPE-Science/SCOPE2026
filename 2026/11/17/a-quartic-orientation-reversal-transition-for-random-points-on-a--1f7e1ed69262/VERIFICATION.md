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

## Reproducible checks

Run `python CHECKER.py` with NumPy installed. The code directly evaluates a four-by-four determinant, compares it with the independently derived symmetric-pair identity, checks the cubic blow-up coefficient, proves the stated elementary integral by rational arithmetic, and estimates the sign-polytope volume by a seeded Monte Carlo experiment. The analytical proof establishes the infinite-population theorem; the finite checker cannot independently establish asymptotics or historical priority.
