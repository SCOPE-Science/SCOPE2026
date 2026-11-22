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

# Reproducibility and verification scope

`RESULT.md` contains the analytic proof, including all parameter domains, exact transformations and sign arguments. Execute `python3 CHECK.py` using the standard Python library. It checks two exact strict integer-power inequalities for the triple-age example; exact rational identities at a grid of rational parameters; strict negativity of a quartic derivative over a finite deterministic grid; and numerical critical-point consistency over several positive pool weights. A successful run prints 12,609 supplementary checks.

Analytic proof, not finite enumeration, establishes the complete continuum of parameter values. No experimental-data inference, stochastic error calibration, external independent audit, or historical-priority certification is claimed.
