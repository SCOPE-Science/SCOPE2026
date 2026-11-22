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
# Verification record

The complete positive-net-gain stationary-state count follows from an explicit bijection to solutions of \(z=k\sin z\), strict monotonicity of each positive-sine lobe away from its unique fold, and reflection symmetry. On the pure-feedback parameter line the exact three-dimensional Jacobian has two zero eigenvalues and one scalar multiplier \(z\cot z\). Monotonicity and the unique \(-1\) crossing give exact stability intervals; reciprocal-angle expansions give a sharp inverse-index gain-width asymptotic. Hyperbolic persistence establishes open parameter regions.

The included standalone standard-library checker `verify.py` bisects transcendental fold/flip equations for selected indices, checks gain ordering, equilibrium residuals, multipliers, and the limiting width coefficient. Its test samples are diagnostics only; they are not a proof of a statement over all lobes or all parameters.

Limits: positive net gain for census, pure-feedback line for exact stability intervals, small full-parameter neighborhoods for persistence. No independent mathematical audit has been performed.
