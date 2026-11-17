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

The accompanying `check_star.py` performs exact rational arithmetic over all active leaf subsets for degrees two through eight, independently computes projected values using the scalar threshold equation, and verifies explicit singleton active-face attainers. Its exact checks are finite corroboration; the mathematical argument in `RESULT.md` proves the general all-degree formula. The self-review is described separately in `REVIEW.md`.
