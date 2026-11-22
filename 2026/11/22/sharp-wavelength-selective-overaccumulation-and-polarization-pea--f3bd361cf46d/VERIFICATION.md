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

# Verification of the Fourier-response theorem

The proof is analytic and uses exact invariant-measure generator identities; none of the conclusions below are inferred solely from simulations.

## Independently implemented computations

`checker.py` uses symbolic factorization and differentiates the two response multipliers, solves the speed-memory and invariant-position complex resolvent systems without inserting the claimed answers, and independently integrates the telegraph characteristic function using a two-state second-order ODE. It passed all 72 parameter cases, with small numerical tolerances specified in the code. The source may be executed with `python checker.py` and requires numpy, scipy, sympy.

`simulation.py` uses a midpoint-integrated deterministic flow between random orientation flips to check the small-amplitude regime, not to certify an infinite-time theorem. At a cosine landscape with base speed, flip rate and wavenumber equal to one and amplitude 0.08, the measured and leading-order predicted pairs (density cosine, orientation sine) were:

| Memory time | Measured | Leading-order prediction |
|---|---|---|
| 0.15 | (-0.046826, -0.004598) | (-0.048393, -0.004537) |
| 0.5 | (-0.052387, -0.008924) | (-0.053333, -0.008889) |
| 1.0 | (-0.051735, -0.009940) | (-0.050000, -0.010000) |
| 2.0 | (-0.042293, -0.008876) | (-0.040000, -0.008889) |

These finite trajectories have sampling and discretization errors and finite-amplitude corrections; exact identities and uniqueness of the thresholds follow from the written proof, not from the table. No independent audit is asserted.
