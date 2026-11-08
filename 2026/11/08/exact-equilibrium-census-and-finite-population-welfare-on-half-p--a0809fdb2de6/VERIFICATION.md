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

# Reproduction and limits

Run `python verify_cycle.py` using Python 3.9 or later. It uses only standard-library `fractions`, `math`, and `itertools`, independently evaluates each swap using the moving agents' post-swap payoffs, and checks the complete labeled-ring equilibrium census and welfare extrema for all populations with \(3\le n\le15\). The ordinal utilities are represented by exact integers \(0\) and \(2\), equal to three times the triangular utility with peak \(1/2\) on the only achievable closed-neighborhood fractions.

Observed output:

```
PASS: 55 population instances, 35103 distinct fixed-count cyclic color profiles, 19506 equilibria.
Exact swap condition, stable census, minimum and maximum degree of integration verified through n=15.
```

The infinite formula rests on the four-step mathematical proof in `RESULT.md`, not on finite enumeration. Arithmetic uses exact integer binomial coefficients and rational fractions. No simulations or probabilistic estimates are involved. This reproduction is limited to the degree-two, half-peaked full-occupancy swap model; no external independent validation has been carried out.
