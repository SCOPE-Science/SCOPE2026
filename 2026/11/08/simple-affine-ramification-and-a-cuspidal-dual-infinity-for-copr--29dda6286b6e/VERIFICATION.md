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

# Verification

Reproduce the finite exact tests by running `python verify_chebyshev_dual.py` with SymPy installed. The script evaluates all 73 coprime integer pairs with \(2\le a\le12\), \(a<b\le18\). It directly checks polynomial gcds, Wronskian squarefreeness and degree, leading coefficients, endpoint evaluations and numerical infinity weights, with rational/integer symbolic arithmetic. Passing results:

```
EXACT_CHEBYSHEV_WRONSKIAN_CHECKS_PASS 73
FINITE_COMPLEX_RAMIFICATION_SIMPLE_PASS
DUAL_MAP_DEGREE_AND_INFINITY_WEIGHT_PASS
```

These are finite tests; they do not prove the result for unbounded parameters. The general proof uses the Chebyshev ODE and coprime derivative root separation, followed by the base-point-free Gauss map and birationality under biduality in characteristic zero. Independent mathematical audit was not performed.
