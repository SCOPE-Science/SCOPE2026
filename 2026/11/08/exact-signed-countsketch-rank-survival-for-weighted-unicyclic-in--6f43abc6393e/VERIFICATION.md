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

The theorem is proved analytically in RESULT.md. The program `verify.py` provides independent finite exact-arithmetic checks of the rank formula and the collision classification; its output is in `verification_output.txt`.

The test covers exhaustive bucket and sign assignments for 27 small scenarios, 3,780 seeded exact-rank structural trials at larger small orders, and 94 integer extremum checks. These computations do not prove the theorem for unbounded graph order or real edge scales; the proof does. No conditioning, floating-point accuracy, or full norm embedding bound has been verified. Independent scientific audit has not been performed.
