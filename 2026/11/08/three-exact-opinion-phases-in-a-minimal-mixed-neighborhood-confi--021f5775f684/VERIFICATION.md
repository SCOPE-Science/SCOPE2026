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

# Reproduction and limits

Run `python3 verify.py` with Python's standard library. The checker performs exact-rational directed receptiveness tests for the three-node path, a finite exhaustive branching check at seven parameter values and depth nine, the dyadic-midpoint finite-time law and variance identity, both sharp equality cases, and the explicit intermediate-phase variance formula. The expected final line begins `VERIFY_OK`.

The analysis of almost-sure oscillation, finite-time commitment, endpoint convergence, and limiting variance uses the proof in `RESULT.md`, including independent-edge block arguments. The finite checker is supplementary and is not an infinite-time certificate. The result applies only to the specified static network, update rule, initial opinions, and parameter domain. Publication priority is assessed against the cited source material; unindexed results and inaccessible full text remain limitations. Independent external review has not been performed.
