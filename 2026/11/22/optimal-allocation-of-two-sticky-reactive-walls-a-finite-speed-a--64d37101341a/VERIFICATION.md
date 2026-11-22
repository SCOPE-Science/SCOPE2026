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

# Reproducibility and verification

Run `python checker.py` with Python 3 (standard library only). The checker uses separate backward-boundary linear equations and random rational parameters to reconstruct the first-passage mean, then uses independent golden-section minimization to compare the constrained optimum with the closed formula. It also tests strict optimal-allocation movement with the killing budget and both limiting allocation laws.

Observed test output on the delivered checker:

```
PASS {'exact_backward': 600, 'numeric_backward': 300, 'independent_optimizer': 300, 'budget_monotonicity': 120, 'limits': 120} total 1440
```

All claims for infinitely many parameter values rest on the analytic differentiation, strict endpoint signs, and limiting arguments in `RESULT.md`; numerical samples and exact-rational point tests are diagnostic only. No claims are made about stochastic simulations of full trajectories or independently certified calculations.
