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

The analytic proof supplies the infinite-size statement. Reproduction: install SymPy and execute `python verify.py`. The actual invocation passed 126807 algebraic, rational dual-sign, matrix trace, and exact excess-decomposition checks. The checker explicitly computes the independent matrix resolvent trace \(\operatorname{tr}((I-P+\mathbf 1\mathbf 1^{\mathsf T}/n)^{-1})-1\) for small orders, rather than reusing the cut formula. Tests on finitely many sizes cannot establish the all-size theorem; the positivity of the displayed factorizations in RESULT.md supplies that step. The scientific novelty assessment is based on inspected literature and remains subject to unindexed equivalents. Independent mathematical audit has not been performed.
