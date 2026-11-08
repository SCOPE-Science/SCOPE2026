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

Verification performed with `python verify.py` (Python 3.10+ and SymPy). The checker directly builds every labelled second-moment generator equation on stars with the original independent one-sided updates, solves rational linear systems, and compares centre variances, leaf variances, centre–leaf covariances, and distinct-leaf covariances with the theorem's closed formulas. It also checks exact sign predictions and symbolic size-change identities.

Observed result: `PASS: 608 exact labelled and symbolic assertions`.

The exact tests sample finite parameter families, while the infinite family of graphs and all real \(0<\theta\le1\) are proved analytically by generator balance and factorization in RESULT.md. No finite experiment is asserted to establish an infinite theorem, and no independent external audit has been carried out.
