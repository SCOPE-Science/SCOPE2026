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

The full proof is in RESULT.md. Execute `python check_philip.py` with Python 3 and SymPy installed. The diagnostic was run on the exact accompanying source and yielded `11203 assertions passed`. The checker uses symbolic simplification for critical shape identities, deterministic randomized exact-model recovery and local nonuniqueness examples; finite checks do not prove global injectivity.

The main analytic safeguards are the correct normalized second divided difference, positive sorptivity, strict ordering of four distinct timestamps, and an onset strictly preceding the first time. The upper ratio boundary is excluded because the onset is required to be strictly earlier than the first observation. The linear coefficient is checked independently for strict positivity; the gauge offset is unrestricted in the main theorem. The clock-origin shape ratio degenerates towards one for remote onset, so no claim of uniform numerical stability is made.
