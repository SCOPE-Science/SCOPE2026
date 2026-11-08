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

The exact algebra and finite numerical scenarios can be reproduced using Python 3 and SymPy:

```sh
python verify.py
```

Observed output:

```
EXACT_IDENTITIES map_derivative=1 cusp_factor=1 cubic_jet=3 log_cancellation=1 infinite_step=2
FINITE_ORBIT_SCENARIOS 10
VERIFY_OK exact_algebra_plus_finite_checks; asymptotics_require_analytic_proof
```

The script explicitly checks the zero quintic term and the unique logarithmic cancellation step. Ten finite orbits represent five positive step regimes, including the infinite-step limit, with initial conditions on opposite sides of the cusp. These computations cannot establish global convergence for all initial populations or the infinite-time expansion. Those statements require the derivative, exact cusp factorization, inverse-square recurrence and summable-remainder arguments in RESULT.md. No independent review has been conducted.
