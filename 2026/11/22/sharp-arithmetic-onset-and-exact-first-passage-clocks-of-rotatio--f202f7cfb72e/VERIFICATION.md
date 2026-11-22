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

## Checks performed
The embedded `CHECK.py` independently computes Boolean one-sided erosion and all cyclic rotation invariances from bits. It tests the exact onset-time formula on every state of rings 2 through 12, all nonzero shifts, all integer times from zero through the ring size, and confirms the independent pre-extinction onset criterion for all initial states of rings 2 through 16. Actual outputs: 81,924 state-shift clock tests; onset counts for n=2..16 are 0,0,0,0,0,0,0,0,10,0,48,0,238,30,912. It prints `PASS` on success. The universal proof is by run-profile identities and does not rely on a finite test horizon.

No external or independent mathematical audit has been performed. Reproduce via `python3 CHECK.py`.
