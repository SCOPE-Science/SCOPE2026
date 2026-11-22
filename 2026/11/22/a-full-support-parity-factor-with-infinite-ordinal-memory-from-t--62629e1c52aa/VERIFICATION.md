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
Run `python3 verify_parity_skew.py` with standard Python 3. The checker implements inverse-image interval lengths directly from skew tent maps, compares the independent-source parity cylinder probability with the derived two-state substochastic recurrence, and checks the all-zero Hankel identity using exact `fractions.Fraction` calculations. Four rational parameter pairs and lengths through eight give 84 checks; no floating-point tolerance or external library is required. The mathematical proof handles every real interior parameter and all lengths; finite checks alone do not establish universality.

Self-review: passed. Independent audit: not yet performed.
