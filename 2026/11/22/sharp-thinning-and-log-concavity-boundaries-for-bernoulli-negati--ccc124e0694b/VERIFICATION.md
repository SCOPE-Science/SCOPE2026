---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility notes

Run `python3 verify.py` in the same directory. The standard-library script computes canonical coefficients by formal division of the normalized pgf series, compares them with their formula, and checks boundary cases and separating examples using exact rational arithmetic. Index 12 gives an obstruction in a case where the comparison at index 2 alone does not detect failure. The all-index and all-rate statements follow from the analytic parity argument and thinning-quotient proof in `RESULT.md`, not these finite illustrations. This version does not claim a new mass-curvature criterion.
