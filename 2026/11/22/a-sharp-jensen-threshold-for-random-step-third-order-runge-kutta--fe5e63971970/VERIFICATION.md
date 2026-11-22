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

`verify.py` is self-contained and uses the Python standard library. It checks rational polynomial expansions, the exact derivative relation for the threshold, the shifted quintic and its exact endpoint signs, and the rational positive witness. It then performs supplementary numerical sampling to corroborate the positive-curvature regime.

The global theorem is proved by the positivity decomposition and Descartes sign-change argument in `RESULT.md`, not by exhaustive numerical sampling. No external or independent mathematical verification has been performed. The conclusions concern one-step squared norm, not accuracy at a common random physical time.
