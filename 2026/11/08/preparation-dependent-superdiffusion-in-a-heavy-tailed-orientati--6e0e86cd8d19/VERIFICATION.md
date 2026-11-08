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

# Reproducibility and checks

The proof is given in RESULT.md. From the same directory run `python checker.py` with NumPy installed. The executable numerically evaluates the angular-reward Laplace transform two ways, tests the exact fresh/equilibrium coefficient identities, and runs fixed-seed simulations of the two renewal-count initializations. All deterministic assertions passed when checked from the final package. The simulations check convergence only and do not prove any infinite-time statement.

For the illustrative parameters \(lpha=3/2\), \(	au=d=v=1\), the predicted reset-count variance constants are \(1/3\) and \(2/3\), while the corresponding physical longitudinal constants are approximately \(0.0781678570\) and \(0.1563357141\). This example is a finite diagnostic of formulas proved analytically for every allowed parameter.

Scientific caveats: the proof uses the monotone-density renewal Tauberian argument for the smooth Lomax law and assumes a correctly coupled equilibrium renewal age and forward residual. Finite-sample error, sensitivity to non-Lomax tails and physical reproducibility are not certified. Independent audit is not yet performed.
