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

# Reproducibility details

The attached `verify.py` is the complete standalone verification diagnostic. Run it with `python verify.py` using Python 3, `sympy` and `mpmath`; the program prints a `VERIFY_OK` message if all assertions hold. It checks the logit conjugacy and derivative symbolically, the odd critical-map Taylor coefficients exactly, four forced periodic return orbits and their phase-average identities with high precision, 24 initialized trajectories, three slow critical tails, four known supercritical two-cycles, and three bounded aperiodic input trajectories.

Those finite checks are not exhaustive in the forcing sequence, period, parameter, initial value or time horizon. Global convergence, phase uniqueness, all-input synchronization and the critical law are analytic results proved in `RESULT.md`. No independent scientific audit or external certification is claimed.
