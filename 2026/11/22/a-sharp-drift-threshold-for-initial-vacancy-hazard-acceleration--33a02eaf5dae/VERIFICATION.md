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

The proof derives the general hazard and threshold symbolically from the exact uniform stationary law, flux-weighted entrance distribution, killed generator and hypergeometric factorial moments. An independently constructed full configuration generator was checked using exact rational arithmetic for every charge sector on rings of length 4 through 8 and six positive rational pairs of jump rates (150 tests). Run `python3 check_hazard.py` in the same directory; no third-party packages or data files are needed. These finite calculations check the formulas but are not exhaustive over size or real rates. The infinite family and threshold uniqueness are obtained by the displayed algebraic proof, not by numerical interpolation. No independent scientific audit is asserted. The conclusions concern only the derivative at the start of a vacancy spell initiated at a stationary departure event.
