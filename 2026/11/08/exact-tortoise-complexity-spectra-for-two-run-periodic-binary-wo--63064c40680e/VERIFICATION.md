---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

The standalone `verify.py` checks finite examples of the final one-iterate theorem for \(a,b\ge2\), explicitly comparing two implementations of the tortoise map, the predicted class count, and the unique collision pair at each intermediate length. The mathematical proof applies for all integers \(a,b\ge2\) and \(n\ge1\); finite tests alone do not imply unrestricted correctness. No formal proof or external expert attestation is asserted.
