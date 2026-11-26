---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

## Reproducible checks

Run `python3 radial_inverse_check.py` alongside this file. It uses standard-library exact rational arithmetic to solve two radial Poisson equations in succession on the cube. For every dimension from 2 to 30 it compares the result with all Walsh shell entries and checks the signs, strict ordering, antipodal harmonic formula and exact Parseval normalization. It does not establish originality or any asymptotic from sampling. The credited exact angle formula, monotonicity and the error estimates are explained in `RESULT.md`.
