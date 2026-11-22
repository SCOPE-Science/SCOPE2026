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

# Reproducibility checks

Run `python verify.py` with SymPy, NumPy and SciPy from this directory. It reconstructs the generator directly from the six transition rules, solves the stationary and marked-count Poisson equations, verifies every integer coefficient in `certificate.json`, proves the sign-variation counts by exact integer arithmetic, verifies rational root brackets, and independently propagates count moments using a 24-dimensional linear moment system for five positive rational adsorption rates.

Observed execution: all four exact formula/derivative sign verifications and 20 independent moment-ODE comparisons passed. The polynomial sign argument, not the finite tests, establishes the theorem over every positive control rate. No external/independent audit has been performed.
