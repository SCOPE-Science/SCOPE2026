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

# Reproduction

Execute `python verify.py` with Python 3.10 or newer. It uses only Python's decimal module. It checks the exact first-exit prefix identities for four bases and three small perturbation sizes, directly evaluates the truncated Parry-type step density and its invariant first moment, and integrates the density difference on all induced intervals to check the predicted asymptotic ratios.

Numerical output is a finite corroboration; the analytical tail bound and positivity are supplied in `RESULT.md`. The checker does not independently establish all-parameter convergence. The reviewed proof establishes the theorem at each fixed real base greater than one.
