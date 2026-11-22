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

The accompanying `checker.py` uses exact rational arithmetic for the mean/second-moment and fifth-order normal-form identities. It explicitly checks a positive logarithmic coefficient \(11/80\), a negative coefficient \(-1/20\), and a zero coefficient. Finite double-precision trajectories of 400,000 steps provide consistency checks on the logarithmic residual; their agreement is not used to certify the infinite-time limit.

The mathematical argument is independent of finite iteration: a block comparison establishes global extinction, the center spectrum has exactly one unit root, a local center manifold and stable tracking justify the fifth-order scalar reduction, and the inverse-square increment has a summable remainder after the two moment coefficients are substituted. The horizon-four equality case follows from an exact quadratic lower bound; the five-lag negative example is rational and explicit.

Limits: only fixed finite memory, nonnegative normalized weights with positive endpoints; logarithmic asymptotics require an initially strictly positive history in \((0,1]^{m+1}\). No independent proof audit, formal verification, or empirical validation of infinite-time behavior has been performed.
