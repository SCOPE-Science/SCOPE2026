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
# Verification and scope

Invoke `python3 verify.py` alongside `RESULT.md` with an ordinary Python 3 interpreter. The script has no non-standard dependencies, and its current execution completed 942 assertions. Checks cover the exact rational parameter threshold, sign factorization, entropy lower bound, exponential-series estimates, first-moment matrix spectral consistency, and several parameter-domain cases.

The finite parameter checks are not substitutes for the all-parameter proof. Almost-sure negativity is not established by simulations: it is derived in `RESULT.md` using the Riccati comparison, a positive-frequency lower bound for long exponential holding intervals, and the bounded-jump martingale strong law. The stated rational exponent bound is certified analytically, not estimated numerically.

This package has undergone self-review only; independent audit or empirical validation has not been performed. The limits include an idealized linear two-patch model, environment switching independent of population, and positive initial conditions.
