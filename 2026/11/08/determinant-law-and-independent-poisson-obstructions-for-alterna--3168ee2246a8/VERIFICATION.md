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

# Reproducibility and verification

Run `python checker.py` with a standard Python installation. Expected final line: `MATCHING_MODAL_DETERMINANT_EXACT_OK 12 CYCLE_EXPECTATION_CHECKS 15`. The checker enumerates exact finite models and rational marking probabilities as described in RESULT.md. The infinite coefficient identity is proved combinatorially; the Poisson limits and spectral asymptotics are justified analytically, not claimed as results of enumeration. Additional independent review has not been performed.
