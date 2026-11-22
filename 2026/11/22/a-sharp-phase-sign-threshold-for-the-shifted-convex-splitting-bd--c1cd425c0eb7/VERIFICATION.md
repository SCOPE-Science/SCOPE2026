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

The theoretical proof is in `RESULT.md`. It covers all real timesteps and all sufficiently small exact-start amplitudes; its signs are not inferred from simulations. The auxiliary `verify.py` reproduces symbolic identities for the implicit cubic derivative and discriminant, checks the mapping's oddness, and computes finite representative sequences near and away from the critical value.

Run `python verify.py` with Python 3, SymPy and SciPy. In the checked execution the script completed all symbolic assertions and all twenty finite parameter checks, printing `symbolic checks PASS`; the observed finite sign patterns matched the analytical regions. A finite run cannot verify infinitely many signs, global uniqueness of published priority, or arbitrary-parameter PDE behavior. No independent mathematical review or external certification was carried out.
