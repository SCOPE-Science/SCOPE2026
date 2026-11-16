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

The attached `verify.py` independently enumerates all domino tilings for grids of size 3 by 2, 4 and 6, tests the alternating-column signed sum, and compares with exact 2-state recurrences. For 3 by 2 and 3 by 4 it performs the full integer Walsh transform of the edge-incidence indicator, verifying every coefficient. The recurrence and signed unit values are also checked for 500 widths. The all-length proof is supplied in `RESULT.md`; finite computations are corroborating evidence only. The checker was executed from its actual packaged contents. Independent mathematical validation has not been performed.
