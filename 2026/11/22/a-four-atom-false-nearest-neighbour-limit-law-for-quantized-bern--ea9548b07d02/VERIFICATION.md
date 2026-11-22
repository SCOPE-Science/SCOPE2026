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

# Reproduction
Run `python3 CHECK.py` using Python 3 standard library only. This verifies the first-hit joint law for 19 rational biases, the moment identities, and three fixed-seed length-300,000 empirical FNN comparisons. The proof of almost-sure convergence and first-hit independence is in RESULT.md; finite tests do not certify it on their own.

The observation is binary, the sample contains one more observation than time-delay vectors, and ties select the earliest different index. The numerical checker does not test variants using different tie-breaking, additive noise, or continuous observables. The scientific argument should be assessed independently before reuse as a general FNN inference result.
