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

# Reproducible checks

Execute `python check_whirling.py` with SymPy, SciPy and NumPy. It checks three polynomial differential identities, a triple-root cusp identity, an explicit strict three-positive-root example, and the exact cubic coefficient of the center equation. Two numerical trajectories illustrate the predicted critical inverse-square decay.

The proof of convergence for all initial states and all detunings is analytic: it uses dissipative inequalities, strict critical-height monotonicity, planar Bendixson–Poincaré arguments and asymptotically autonomous perturbation comparison. The numerical checks are not exhaustive and cannot establish historical priority. The earliest source used was publicly posted November 4, 2026. Earlier whirling-string papers were not available for complete-text comparison; independent validation has not occurred.
