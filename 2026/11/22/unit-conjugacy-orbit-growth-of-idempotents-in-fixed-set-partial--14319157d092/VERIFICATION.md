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

# Reproducibility and scope of checks

Run `python3 scripts/check.py` using Python 3.10+ from the extracted file package; no third-party Python modules are needed. The checker exhaustively enumerates all admissible partial maps and tests idempotency for all \(0\le a\le3\), \(0\le b\le4\). It groups maps by the directly computed decorated-star signature, constructs every actual unit-conjugacy orbit, and checks sizes against the stabilizer formula. It separately verifies labeled rank counts and the orbit-count generating-function coefficients.

Expected final line: `FIXED_POINT_PARTIAL_RETRACTION_ORBITS_VERIFIED`.

The finite checks do not establish the theorem for larger sets. The infinite classification is proved by the rooted-star normal form and orbit-stabilizer argument, and the asymptotic rests on the classical partition estimate and coefficient analysis shown in `RESULT.md`. A finite computation does not validate the historical-priority assessment.
