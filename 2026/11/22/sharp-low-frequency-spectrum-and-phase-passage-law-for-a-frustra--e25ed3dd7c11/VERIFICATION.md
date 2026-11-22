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

Run `python3 verify.py` with Python's standard library to check exact ground-state graphs and rational hitting-time linear systems for sizes 1 through 3. The recorded output was `EXACT_GROUND_WALK_CHECKS_PASSED 9`. Optionally install `requirements.txt` and run `python3 spectrum_check.py` for a weighted-radial-quotient numerical check of spectral scaling through size 28. Both programs were run with the code included here. The general spectral limit is supported by the explicitly derived Green-matrix capacity lemma and min–max argument, not the numeric comparisons. No independent external audit was conducted.
