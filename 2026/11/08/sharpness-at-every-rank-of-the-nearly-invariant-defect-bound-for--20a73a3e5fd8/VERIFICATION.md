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

Run `python3 verify.py` with Python 3.10 or later. The checker uses only the Python standard library and computes exact rational ranks for \(r=1,\ldots,7\). It verifies the matrix definition, perturbation rank, graph kernel, quotient kernel, and exact shift-defect dimension in these seven finite cases. The proof for every positive integer rank is the analytical graph/quotient argument in `RESULT.md`; checking finitely many cases does not establish that universal quantifier.

The first-public date (2026-10-29) and primary MSC (47B35) are verified at https://arxiv.org/abs/2610.40295. The cited upper bound is [1, Theorem 5.4]. This is a self-reviewed finding; no independent mathematical audit has been performed.
