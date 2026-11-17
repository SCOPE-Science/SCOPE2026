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

# Reproducible verification

Run `python3 verify_period.py` with Python 3.10 or later. The checker uses only the standard library and evaluates an independent numerical quadrature of the exact angular formula, determining the energy-dependent radial intersection by monotone bisection.

The tested quantities are \(T_\theta(E)\) for five weights, the local slope \(\theta/8\) for three weights, the singular crossover \(\varepsilon T_{1-\varepsilon}(e/\varepsilon)\) for four positive scaled energies and two mixing weights, and three fixed-endpoint large-energy comparisons. Expected output:

```
VERIFY_OK strict_period_cases=5 small_energy_checks=3 crossover_parameters=4 high_energy_cases=3
```

These tests are finite numerical consistency checks, not a proof of global monotonicity, exact asymptotic limits or historical originality. The analytical arguments are in `RESULT.md`, especially the strict angular-speed comparison, dominated convergence for scaled contours and explicit quadrant arc geometry. The independent audit status is not performed.
