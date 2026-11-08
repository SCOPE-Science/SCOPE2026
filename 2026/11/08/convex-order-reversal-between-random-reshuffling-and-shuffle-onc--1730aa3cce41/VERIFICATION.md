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

# Verification record

- Reproduce with `python verify.py` using Python 3.9+ (standard library only).
- The program enumerates exact rational output distributions, checks equal means and stop-loss inequalities at every support breakpoint (equivalent to convex order in one dimension), and compares two- and three-component SGD orders over 50 independent finite-horizon cases.
- The program verifies the exact stationary example \(A=-1/8\), \(\operatorname{Var}(B)=81/64\), \(\operatorname{Var}(X_\infty^{\mathrm{RR}})=9/7\), \(\operatorname{Var}(X_\infty^{\mathrm{SO}})=1\), and objective-gap \(3/14\).
- The exact proof establishes arbitrary dimension, all convex test functions, every epoch count and stationary limits; finite checking does not certify any universal quantifier.
- Source comparisons and a self-review were conducted, but independent scientific audit and exhaustive publication-precedence validation have not been performed.
