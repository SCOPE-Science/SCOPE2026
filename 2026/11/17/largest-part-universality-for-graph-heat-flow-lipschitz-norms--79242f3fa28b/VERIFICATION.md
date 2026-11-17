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

# Computational verification

Run `python verify_multipartite_heat.py` with Python 3 and no third-party libraries. The checker uses exact rational arithmetic for the heat kernel, its row sums and exact semigroup law, and for the maximization over all anchored integer-valued Lipschitz potentials on 15 complete multipartite graph profiles at four rational values of \(q=e^{-t}\). The upper and lower Lipschitz constraints have integral incidence matrices, so their finite-dimensional vertices are integral after fixing a basepoint; diameter two bounds the enumerated range.

Observed output:

```
EXACT_EXHAUSTIVE_EDGE_DUAL_OPTIMIZATIONS_PASSED 412
TOTAL_FEASIBLE_INTEGER_LIPSCHITZ_POTENTIALS 1103
EXACT_HEAT_SEMIGROUP_IDENTITIES_PASSED 60
ALL_MULTIPARTITE_HEAT_NORM_CHECKS_PASSED
```

These finite cases are diagnostics. The universal formula, threshold, peak, monotonicity and asymptotic claim require the analytic derivation in `RESULT.md`, not an inference from numerical samples. Independent mathematical audit has not been performed.
