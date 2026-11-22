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

## Reproducibility
Execute `python check.py` with Python 3. No external packages are required. The program enumerates graph edge subsets, checks acyclicity, enumerates distinguished component roots, computes the full Walsh transform, and compares it to the closed form for n=2,3,4. An independent Bareiss determinant evaluates every shore-character class through n=7. Every parameter class from n=2 through n=60 is checked against the exact zero criterion and associated binomial multiplicity.

## Verified mathematical boundaries
The determinant factorization requires n>=2 because its Schur diagonal blocks contain n-1. For n=1 the claimed odd-parity singularity does not apply. The all-n rank formula follows from the displayed algebraic argument; finite checks are not an infinite proof. No independent assessment has been performed and no sharp smallest-nonzero singular value is claimed.
