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

# Reproducibility checks

Run `python checker.py` from the same directory with Python 3 and SymPy. The script independently rebuilds the spectral resolvent, compares all complex entries, checks the dimensionless derivative and exact limiting ceiling, and checks 144 rational parameter comparisons. No randomized seed, numerical spectrum fit, or external dataset is required. These computations corroborate, but do not replace, the complete analytic sign and monotonicity proof in RESULT.md.

An independent scientific audit has not been performed. The asserted bound applies only to the model and spectral definition stated in RESULT.md.
