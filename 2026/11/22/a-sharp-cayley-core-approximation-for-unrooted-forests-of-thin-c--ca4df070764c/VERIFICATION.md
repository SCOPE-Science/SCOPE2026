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

This package includes `verify.py` and uses only Python's standard library. Execute `python3 verify.py` in the directory containing the extracted files. This program performs independent direct edge-subset exhaustion, a special-neighborhood hyperforest count, and a component-anchored recurrence, then verifies the first two coefficients and numerical consistency of the sharp first-order probability constant.

Expected final line: `VERIFY_OK`. Its finite checks are not a proof of the infinite-parameter statement; the proof in `RESULT.md` classifies all dominant neighbourhood patterns and bounds the remainder for every fixed first-shore size. Errors in unseen parameters would require mathematical review, not merely matching test output.

The exact conditional law is verified mathematically by a count-preserving bijection; total variation is exactly the probability of the omitted finite event. No Lean or third-party certificate is claimed, and no independent review has been performed.
