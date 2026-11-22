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

The included `checks/check.py` is a standalone Python standard-library checker for the exact moment inversion, the region inequalities, random nonmonotone meridian trajectories, the extremal ratio formula and finite-damping GKSL Bloch simulations at small noise rates. Invoke `python3 checks/check.py` from the extracted package directory. The checker passed 4,445 assertions on the packaged source.

This is finite consistency testing. The rigorous assertions for all admissible controls and all error-pair coordinates are proved in RESULT.md by the positive residual occupation measure, the two-moment inequalities and the constructive two-dwell pulse. The ODE tests compare finite-\(\gamma\) error slopes to the calculated first derivative; they do not establish any finite-\(\gamma\) optimization theorem. No independent scientific audit has been performed.
