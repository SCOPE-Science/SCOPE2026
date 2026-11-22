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

# Verification and limits

`python check.py` enumerates every partial isotone map on chains of lengths 2, 3, 4 and 5. It checks each nonempty proper cut, every predicted joint domain-size/image-rank cell, and maximality by an explicit singleton-map witness for every possible excluded map. It independently checks the Fibonacci size-profile totals 3, 8, 21, and 55 (including the formal empty-cut representative). All tests passed. The general proof is in `RESULT.md`; computations do not certify arbitrary chain lengths.
