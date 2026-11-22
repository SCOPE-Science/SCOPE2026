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

Run `python check.py` from the extracted package with Python 3. The script performs 12,802 exact rational assertions on the Haar jump normalization, squared-tent calibrated identity, dyadic Parseval, all finite dyadic improvement expressions, repeating two-cycle, finite-scale upper bounds, and telescoping. A pass is evidence of consistency only: every infinite-scale bound, the equality-case classification, the critical coefficient and the weak-limit theorem require the analytical arguments in RESULT.md.

The 2003 source's publisher date is documented as 2003-04-30, and the 2016 fixed-scale Haar source as online 2016-02-15. The original text from those sources was compared directly, but unindexed historical equivalents cannot be ruled out. No independent mathematical validation was performed.
