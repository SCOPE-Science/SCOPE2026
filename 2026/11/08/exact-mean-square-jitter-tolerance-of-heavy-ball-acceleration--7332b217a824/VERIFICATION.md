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

# Verification scope

- Exact symbolic identity for modal characteristic polynomial and Lyapunov covariance, using SymPy.
- Strict positive-definite covariance comparison and crossing at a unit moment root.
- Derivation of largest-eigenvalue modal condition and classical Chebyshev HB tuning.
- Exact two-point noise counterexample with positive random step multipliers; strict GD stability.
- Exhaustive rational sign-path enumeration up to eight steps for selected initial conditions and both eigenvalues.
- No Monte Carlo evidence required for universal statements; no independence/certification by an outside party.

The code requires SymPy and uses Python exact `Fraction` arithmetic. `verify_output.txt` is the captured output from the delivered standalone checker. The finite enumerations are consistency checks only: the published claim depends on the displayed analytic Lyapunov comparison. The model does not include correlated jitter, nonpositive curvature, adaptive parameters, or arbitrary nonquadratic objectives.
