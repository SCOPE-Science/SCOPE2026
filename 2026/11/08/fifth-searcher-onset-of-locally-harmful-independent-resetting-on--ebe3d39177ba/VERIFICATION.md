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

# Exact arithmetic verification

Run `python verify.py` in this directory. The script uses only Python's standard library, and constructs the continuous-time killed generator from the four transient vertices of the path. It computes exact rational means and independent-reset first derivatives for populations one through five, checks all linear residuals exactly, and asserts the five stated fractions and signs. An independently defined labeled-walker chain reproduces both mean and first derivative for one, two and three walkers. This is a complete finite verification for the specified five population sizes and no others. It is not a proof of a global reset optimum or of monotonicity after the fifth walker.
