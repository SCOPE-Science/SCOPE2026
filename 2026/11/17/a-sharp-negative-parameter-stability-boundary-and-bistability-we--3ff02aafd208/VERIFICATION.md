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

# Verification details

Running `python artifacts/verify_negative_etm.py` with SymPy reproduces the exact polynomial discriminants, four algebraic root isolations, Sturm counts at representative rational parameters, origin characteristic polynomial, nonzero-equilibrium determinant reduction, Lyapunov determinant identity, and interval-crossing checks. The saved output is `artifacts/verification_output.txt`.

The infinite-parameter statements are established by continuity plus exact discriminant isolation and by the explicitly bounded Hurwitz coefficients; finite parameter samples alone are not treated as a proof. At each strict value of the negative global-stability interval, the negative-definite quadratic form gives actual global exponential convergence. At the bistability window the two sinks are verified with the full three-dimensional Jacobian rather than scalar stationary reduction alone.

Limits: no independent validation or external certification; no global basin-boundary identification, endpoint relaxation rates, or classification of remote negative-parameter attractors.
