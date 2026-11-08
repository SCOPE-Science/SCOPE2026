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
# Verification

Run `python verify.py` with Python 3; it needs only the standard library. The checker independently enumerates stable configurations, tests recurrence by full once-per-vertex sink burning, directly stabilizes one-grain perturbations, and computes the number of spanning trees of the sink-deletion graph via an integer Bareiss determinant. Seed 371 fixes 207 connected random graphs on three through six vertices and 469 eligible source checks. It further checks both choices of sink on wheel rim sizes three through seven and prints exact formulas through size ten. The test is finite; the general theorem follows from the burning-test bijection supplied in RESULT.md.

Boundary cases: graph deletion disconnects; the full-avalanche count is then zero. Parallel edges are allowed by the proof, though the sampled random graphs are simple. The asymptotic probability requires fixed one-grain addition at a sink neighbor, not a uniformly random source among all vertices. A historically relevant 2017 source could not be checked beyond abstract, and no independent scientific audit has been performed.
