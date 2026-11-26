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

Run `python3 verify.py` with Python 3 (standard library only). It computes the variance from exact integer counts of the three sampled group occupancies and checks both rational identities and their signs at each of the 95 values \(m=6,\ldots,100\). These checks do not substitute for the analytic all-\(m\) sign proof in RESULT.md. The earlier sharp finite census boundary is prior context, not a claim of this note.
