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

The complete proof follows from the exact conditional Brownian-bridge integrated variance and strictly convex expected squared-gap loss. In particular, the all-retained event has positive probability and its Hessian is positive definite; a telescoping Bernoulli-geometric identity makes the proposed grid stationary.

Supplementary exact checks: `python3 check.py` from this package. The actual run is recorded verbatim in `check_output.txt`; 405 exact rational assertions passed for all retention subsets of up to seven candidate times, five rational probabilities, exact derivatives and feasible perturbations. These computations do not establish the infinite-family result by themselves.

Independent audit was not performed. The statement does not cover correlated failures, measurement noise, adaptive locations or other process kernels. The 2012 spatial-estimation source could not be read in full; this limits certainty about historical priority, not the elementary algebraic proof.
