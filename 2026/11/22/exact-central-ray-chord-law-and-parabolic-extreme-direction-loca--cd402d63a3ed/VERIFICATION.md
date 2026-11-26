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
# Reproducibility and scope

Run `python3 verify_localization.py` from this directory. The standard-library script checks the conditional support against the Euclidean radial formula at test directions and numerically compares the area of that support with a scalar spherical cap-overlap calculation. It checks the scale of the TV error and the second moment of the shell height at shrinking positive thresholds. These numerical checks do not certify a limit; the uniform width expansion and exact decomposition in `RESULT.md` establish the sharp rate and weak shell limit.
