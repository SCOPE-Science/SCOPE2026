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

The analytical verification is given step by step in `RESULT.md`: exponential-time Brownian motion is Laplace, Voronoi cells sum to exact transition and reward formulas, finite-state Markov renewal rewards produce the physical-time velocity, and strict monotonicity of the hyperbolic-sine ratio proves the global sign classification. The rate asymptotics follow from Taylor and exponential-tail estimates.

Run `python3 verify.py` from the extracted package. It executes 128 deterministic assertions: independent cell integration, the stated formula at several parameters, zero-current cases, sign checks, weak/strong reset regimes, and fixed-seed simulations that sample the Gaussian Brownian increment conditional on the actual exponential holding time. No external packages or pre-existing logs are required.

Numerical finite checks do not prove the infinite-time almost-sure assertion. Independent audit has not been performed. No external proof certification is claimed.
