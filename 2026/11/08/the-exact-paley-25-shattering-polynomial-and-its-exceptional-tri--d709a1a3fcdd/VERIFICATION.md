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

Run `python3 paley25_verify.py` (standard library only). The script constructs the adjacency table by the norm test, tests all 12,650 four-element supports, partitions the 3,600 shattered supports by all 600 specified maps, and checks the exact representatives, orbit sizes and stabilizer orders. It prints each orbit and ends with `VERIFY_OK supports=12650 shattered=3600 orbits=8`. The analytic bound of 25 centers rules out supports of size five or larger. The program does not assess historical priority, other notions of shattering, or other field orders.
