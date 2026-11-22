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

Run `python3 verify.py` from the directory containing the packaged `verify.py` and `RESULT.md`. The checker uses only Python 3 standard-library exact fractions and enumerates finite attachment histories. It independently compares the law to the generating-polynomial recurrence, verifies lower and upper convex-order inequalities at every integer stop-loss threshold, checks sharp variance bounds and tests the explicit controls realizing arbitrary shifted Poisson-binomial laws.

The checker returned `PASSED 67354 exact assertions` for the packaged candidate. The finite tests do not establish infinite or arbitrary-size claims; the self-contained determinant and convex-order proof in `RESULT.md` is the mathematical basis for those statements.

Independent mathematical assessment has not been performed. The historical-priority uncertainty described in the scientific manuscript remains.
