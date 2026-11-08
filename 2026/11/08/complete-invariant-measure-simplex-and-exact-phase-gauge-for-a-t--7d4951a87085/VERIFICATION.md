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

The standalone program `verify.py` was executed in a Python 3 environment with SymPy, NumPy and SciPy. It printed:

`VERIFY_OK exact_symbolic_jacobian=1 exact_divergence=1 stationary_state_algebra=1 exact_routh_threshold=1 gauge_coefficient_checks=80 numeric_conjugacy_integrations=36 max_error=4.804e-11`

The symbolic checks verify the projected equilibrium factorization, both nonzero equilibrium stability determinants, the exact divergence identity, and an auxiliary local cubic Routh–Hurwitz computation at the inner circle. Numerical integration compares conjugate trajectories at different parameter and initial-state values; its largest absolute coordinate discrepancy is reported above. The rigorous claims about all forward trajectories and all invariant probability measures come from the analytic argument in `RESULT.md`, not numerical enumeration. The primary paper's global pointwise Hurwitz proof is cited as published context and was not replayed here; no independent audit has occurred.
