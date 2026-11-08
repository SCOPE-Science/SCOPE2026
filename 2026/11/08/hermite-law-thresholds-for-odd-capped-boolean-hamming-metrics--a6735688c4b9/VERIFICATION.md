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

Run `python3 odd_cap_walsh_check.py` with standard Python 3. The program independently enumerates Walsh characters in small dimensions to compare Krawtchouk values and uses the exact coefficient recurrence to evaluate critical eigenvalues at larger dimensions. The final success marker is `ODD_CAP_HAMMING_WALSH_CHECKS_OK`. Numerical roots approximate finite thresholds but do not prove the stated infinite-dimensional limit. The analytical proof is in `RESULT.md`, including the large-frequency tail argument and fixed-cap quantifier. Independent validation has not been performed.
