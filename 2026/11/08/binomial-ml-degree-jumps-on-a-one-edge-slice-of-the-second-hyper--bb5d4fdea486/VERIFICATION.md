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

# Verification

The standalone `CHECK.py` recomputes matrix ranks by exact rational row reduction for all nonempty subsets, then recomputes Euler-characteristic inclusion-exclusion and compares with the binomial-phase formula for each integer dimension from 4 through 9. It checks generic rational coefficients and every distinct exceptional coefficient in each dimension. Execution is deterministic, requires only the Python standard library, and prints `ALL_CHECKS_OK`. The proof of every dimension at least seven is the symbolic principal-determinant calculation, cone Euler characteristic and inclusion-exclusion argument in `RESULT.md`; no finite experiment is treated as an infinite proof. No external independent mathematical audit has been performed.
