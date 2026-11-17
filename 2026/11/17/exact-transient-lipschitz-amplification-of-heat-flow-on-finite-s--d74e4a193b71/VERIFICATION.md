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

# Reproducibility

Run `python verify_star_heat.py` with Python 3. The independent spectral-projection calculation is evaluated with exact fractions at rational values of \(q=e^{-t}\), alongside the exact claimed edge matrix and exhaustive input-cube sign patterns for finite test sizes. The analytic proof, rather than finite checks, establishes universal quantifiers. No external certification has been performed.
