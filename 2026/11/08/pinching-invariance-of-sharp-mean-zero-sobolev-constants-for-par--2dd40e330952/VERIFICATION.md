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

The proof uses the Dirichlet Green kernel on each interval and an energy-orthogonal endpoint-difference coordinate. The crucial all-length comparison is \(\beta_i=((T-L_i)(c-1/L_i)-1)/(T(1+L_i(c-1/L_i)))\), strictly positive for at least three edges by Cauchy--Schwarz and zero for two edges. The edgewise diagonal formulas lead to strict midpoint localization and the exact longest-edge comparison.

`banana_bouquet_green_check.py` builds exact rational stiffness matrices, inserts the evaluation point as a vertex, solves a constrained Poisson equation, and includes the exact integrated quadratic source on each segment. It independently checks the diagonal identity and optimality in \(230\) configurations, including unequal lengths, both endpoints, interior quarters, and midpoints. Executed command: `python banana_bouquet_green_check.py`. Observed output:

```
EXACT_NODAL_POISSON_GREEN_CHECKS_PASSED 230
ALL_BANANA_BOUQUET_SHARP_CONSTANT_CHECKS_PASSED
```

Finite rational experiments are corroboration only. The universal strictness and the full equality classification follow from the proof, not exhaustion. The result is not independently audited or externally certified.
