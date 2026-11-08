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

# Reproducibility and scope

Run `python3 verify.py` using Python 3 and only the standard library. The checker independently enumerates restricted-growth-string set partitions and filters noncrossing objects, computes \(R_n\) from interval nesting, and computes size-class counts. It compares exact rational averages, mixed moments, covariance and signs against the proved formulas for every \(1\le r\le n\le9\); the largest ensemble comprises \(4862\) Catalan objects. It also checks bounded numerical approximations for fixed-size asymptotics at selected larger values through \(n=1100\).

The checked program passed \(263\) assertions comprising exact identities/sign checks and bounded numerical asymptotic diagnostics. Infinite universal claims rest on the full formal-power-series derivation in RESULT.md, not on exhaustive checking of small sizes. The cited older marked-block formulas are known; the independently assessed addition is the outer-block mixed moment and covariance sign classification. The historical priority of expressions implicit in broader ordered-tree generating functions has not been definitively settled.
