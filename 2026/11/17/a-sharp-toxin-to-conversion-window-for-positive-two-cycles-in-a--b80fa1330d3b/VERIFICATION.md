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

# Reproducibility and limits

The theorem is proved algebraically in RESULT.md. The standard-library checker `verify_prime_two.py` runs with `python3 verify_prime_two.py` and reports `TOXIC_PLANKTON_TWO_CYCLE_EXACT_OK generic_samples=36 rational_witness=1` on success. It uses exact rational arithmetic for the explicit example and 36 parameter-fiber constructions, checking the two map equations and all positivity constraints without floating-point rounding.

A separate symbolic expansion verified four identities and a limit in the proof. Both computations are auxiliary: finite tests do not establish the theorem for all real parameter values, and the analytic sign argument and limiting construction are essential. Neither long-term stability nor global positivity of the dynamical system has been tested or claimed.

The closest inaccessible article discussing periodic points creates a residual publication-priority risk. Independent audit has not been performed.
