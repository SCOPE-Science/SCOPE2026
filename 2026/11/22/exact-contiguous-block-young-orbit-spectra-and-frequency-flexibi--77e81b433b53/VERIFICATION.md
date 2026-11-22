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

Two standalone scripts were executed from the embedded file contents with Python 3. `check_random_profiles.py` returned 90,312 passing rational sampled cases and 3,240 passing irrational cases (total 93,552). `check_exact_frequencies.py` returned 8,370 passing rational exact-arithmetic profile/frequency cases. The tests cover finite parameter choices, not every word, composition, or frequency limit. The all-parameter claim and the density and entropy assertions are justified by the independent symbolic argument in RESULT.md. External independent audit: not performed.
