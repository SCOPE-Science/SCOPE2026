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

The analytical result follows from the killed Brownian moment boundary-value problem, the standard Poisson-renewal transform, and a strictly decreasing polynomial that has a unique root. A symbolic check verifies the first three radial moments, both sensitivity derivatives, and the exact sign conditions. A separately evaluated confluent-hypergeometric free-exit transform provides high-precision finite-rate comparisons on representative points in each regime and six dimensions.

Reproduction: run `python CHECK.py` with `sympy` and `mpmath`. Output observed: `PASS 97 assertions; all dimension/radius regimes and independent transform computations agree`.

Numerical calculations test examples only. The uniform claims in dimension and starting radius are proved by exact recurrence and algebra. The result concerns first-order weak-reset effects; no assertion is made at positive finite reset rates uniformly close to thresholds. No independent audit has been performed.
