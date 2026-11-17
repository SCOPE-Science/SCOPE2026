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

# Verification and reproducibility

The exact proof is in `RESULT.md`, with the down-set projection reduction, the sharp Cauchy–Schwarz equality certificate, bipartite path integrality, and a positive dual-multiplier certificate for every path dimension. The cycle result follows from an explicitly represented orbit average of a maximum independent set, and uniqueness of the deepest cube point follows from strict coordinatewise inequality for the projection.

Run `python3 verification/verify.py` with Python 3, NumPy and SciPy. The actual successful replay reported:

`CUBE_STABLE_SET_PARITY_PASS exact_paths=299 exact_cycles=298 independent_qps=24 cube_corner_checks=486`

Exact `fractions.Fraction` checks reconstruct all path edge multipliers, stationarity and squared-distance formulas at orders 2 through 300. Exact cycle maximum-set averaging identities are checked at orders 3 through 300. Independently formulated SLSQP quadratic programs check projection coordinates and objective values at orders 3 through 14; additional comparisons evaluate every alternative cube corner at orders 3 through 7. Numerical tolerances are fixed in the supplied checker. Its finite tests cannot prove the infinite assertions and are not independent mathematical validation. This record does not report an independent external audit.
