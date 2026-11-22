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

The equilibrium equation and its unique positive solution are established analytically in RESULT.md. The derivative identity (1) and endpoint comparison (3) are the decisive symbolic checks. The strict monotonicity of \(Y(R)\) and all boundary cases are proved rather than inferred from finite sampling.

The standalone `CHECK.py` requires only Python 3 and the standard library. Executing `python3 CHECK.py` checks exact-rational values at one endpoint equality, the closed-form minimum in the illustrative case, and randomized finite-sample diagnostics for equilibrium, derivative signs and endpoint signs. In the packaged run it reported 3,614 passing assertions. Numerical tests are supplementary, not a substitute for the analytic infinite-domain proof.

The classification is conditional on positive rates, exponential profiles, positive Holling-II handling time and the local steady-state model. No independent audit or ecological field validation has been performed.
