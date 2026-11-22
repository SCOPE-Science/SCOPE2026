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

# Reproducibility and scope

The standalone `checker.py` uses Python 3, NumPy, exact rational arithmetic and a deterministic seeded simulation. Run `python checker.py` from the directory containing this file.

The program verified 316 assertions: independent-set coefficients and exact factorial moments for sample sizes 2–15; numerical transfer-integral comparisons for selected samples and thresholds; a recurrence-based large-sample Rayleigh check; and a simulation of 60,000 ten-stratum samples (seed 20261116). The exact ten-stratum no-exceedance probability at deficit 1/3 is approximately 0.5805607419261969; simulation gave approximately 0.579.

Proof of all-size identities and the spatial point-process limit appears in `RESULT.md`; computational checks alone do not establish those infinite statements. No independent external mathematical verification is claimed.
