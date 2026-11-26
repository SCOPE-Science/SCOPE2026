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

The accompanying `checker.py` uses exact rational arithmetic to enumerate all two-parent histories up to six vertices and compare the triangle mean and variance with their formulas. Other moments and cross-moments in that script are known identities included as checks, not findings claimed here. The script also checks a finite sign pattern for the local triangle corrections and a rational upper bound on their sum to infinity. The proof for all sizes and the limiting constant are in `RESULT.md`; the bounded enumeration is supplementary.
