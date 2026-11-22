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

# Reproducibility and limits

Run `python checker.py` using Python 3 with its standard library. The checker compares the planar generating function against every rank permutation and every retained-core subset up to union size seven, verifies exact conditional moments, tests dimension-two and dimension-three maxima mean identities for small sizes, and directly enumerates small paired samples whose retained vectors agree. It completed with 194, 172 and 12 assertions in its three stages. No external data or downloaded software is needed.

The argument for all sample sizes appears in `RESULT.md`; finite checks cannot establish infinite convergence. Key external inputs are classical one-sample Pareto-maxima expectation and variance asymptotics from the cited primary literature. No independent mathematical audit has been undertaken.
