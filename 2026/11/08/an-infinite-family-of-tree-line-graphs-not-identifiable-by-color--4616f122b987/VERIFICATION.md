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

Run `python3 verify.py` with Python 3.8 or newer, without third-party libraries. The program constructs five instances (parameters two through six), reconstructs the four degree classes, checks exact adjacency quotients, checks joint color refinement across repeated iterations, and independently counts all triangles. It asserts the exact deficit \(4m-4\) for each instance. The proof, not these finite tests, establishes all infinitely many instances. No independent audit has been performed.
