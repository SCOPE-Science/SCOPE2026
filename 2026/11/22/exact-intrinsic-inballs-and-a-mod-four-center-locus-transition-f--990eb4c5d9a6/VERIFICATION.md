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

## Reproduction and limits

The odd-order part of the unchanged `verify.py` (Python 3, standard library only) uses the intrinsic rational normal equations to compute and compare the exact squared norms for every facet at odd orders 3 through 25. The script also contains even-order comparisons; these are outside the corrected claim. The alternating recurrence and the facet inequalities in `RESULT.md` prove the odd-order formula and uniqueness; finite comparisons are corroboration, not the proof.
