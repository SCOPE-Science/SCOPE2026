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

# Reproduction and verification notes

Run `python3 verify.py` from the directory containing this document. It uses only Python 3 standard-library packages (`math`, `cmath`, `fractions`). The actual run returned:

```
CHECK_OK base=5 period_two_base_cycles=2 threshold_sweep=400 crossover_slope=verified
example_mu=0.3 epsilon_star=0.866038843300
```

The checks include exact rational enumeration of the five cat-map points fixed by its second iterate, explicit formation of two successive fiber Möbius matrices, determinant-one and independently derived trace identities, numerical fixed-circle-point classification away from tangencies, nonidentity at all four sample tangencies, full parameter-order sweeps in both regimes, and an independent centered finite-difference check of the analytic crossing slope.

The complete universal proof is in `RESULT.md`. No number of numerical samples proves that an orbit classification holds for all allowed real parameters; the determinant argument and the monotone Möbius trace supply that proof. No global attractor claims, arbitrary-phase claims, or independent mathematical verification are included.
