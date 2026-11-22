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

Run `python3 checker.py` in a directory containing this file and the sibling script. Its deterministic seed and standard-library computations yield `QUARTIC_STEINHAUS_HILBERT_FINITE_CHECK_OK 88542`.

The principal claim follows from the complete analytic argument in `RESULT.md`. The code exercises finite perturbations, exact constructed maximizers, strict distance order and reciprocal-radius scaling. It does not check all real parameters and it does not constitute an independent mathematical audit.
