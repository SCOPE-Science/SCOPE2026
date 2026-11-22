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

# Reproducible checks

To reproduce finite-degree computational spot checks, run `python check.py` using Python 3 with SciPy and NumPy installed. The checker calculates each candidate Beta absolute moment using regularized incomplete Beta functions, independently integrates binomial survival/CDF step errors on both sides of the same jump, and compares the two. It tests degrees 2, 3, 7, 13, 29; several Stancu strengths; and representative node indices on both sides of each selected node. It then compares the exact maximum of the Beta formulas for degrees 200, 1000 and 4000 with the stated sharp limiting constant across strengths including values on either side of the threshold.

Observed passing markers:

```
BETA_VS_DIRECT_BINOMIAL_STEP_INTEGRALS_PASS
PHASE_TRANSITION_ASYMPTOTICS_PASS
```

The direct numerical integration is independent of the special-function expression used for the finite maximum. The finite sequence is not a proof of asymptotic convergence and small finite degrees can favor an interior jump even when the limiting winning site is an endpoint. The universal theorem is proved in `RESULT.md` by the BV step decomposition, Beta order-statistic CLT, uniform integrability and the Gaussian monotonicity identity. Neither code execution nor these notes claim an external certification.
