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

Run `python3 code/verify_orientation.py` with Python 3 and its standard library. It checks every path orientation through eight vertices, uses reversal/complement canonical keys, and independently enumerates ternary patterns through six vertices and for both eight-vertex witnesses. The deterministic recorded output is `verification/output.txt` and ends with `VERIFY_OK`.

The program directly verifies the first-collision classification but does not prove the homogeneous extension property. That property follows from free amalgamation; the general transfer identity follows from local forbidden-triangle reasoning. No independent audit has been performed.
