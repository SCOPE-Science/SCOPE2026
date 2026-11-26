---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

# Reproducible checks and their limits

Run `python3 verify_constraints.py`. This exact, bounded standard-library computation checks seven reduced incidence profiles and samples the adjugate evaluation identities on integer triples. The proof uses the corrected line-only double-point count \(21-3u\); \(21-3u-v\) counts only the off-conic line double points. The profiles that survive the numerical inequalities require the four geometric cases in `RESULT.md`. Neither the enumeration nor the polynomial samples prove those cases or the cited geometric inequalities.
