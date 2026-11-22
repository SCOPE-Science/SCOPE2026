---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The cube is invariant; for active max/min rows the Dobrushin inequality bounds input diameter by delta(W)D and logistic secants by 1/4, yielding D+ <= -(1-beta*delta/4)D. At equality strict secant dissipation and compactness give D->0; the mean obeys a scalar asymptotically autonomous analytic ODE with finite equilibrium zeros, hence reaches one. The two-site antisymmetric reduction zdot=-z+(1/2)tanh(beta*delta*z/2), monotonicity of tanh(v)/v, full Jacobian -I+beta(1/4-z_*^2)W, and critical z^-2/t->8/3 establish claimed existence, stability example and tD^2->3/2. Reviewed actual RESULT and finite checker; finite trajectories are not proofs.

## originality

FAIL

FAIL: exact published November 2 theorem already proves global homogenization for beta*delta<=4 (including high-beta multistability), strict rate, critical 3/2 contrast coefficient, two-node existence and its complete stability thresholds. The stronger October 18 theorem establishes exact nonlinear diameter comparison even for shared time-varying forcing. The new claim is mathematically covered without requiring identical wording.

## value

FAIL

FAIL: after full prior-theorem implication, no independent unknown meaningful mathematical fact remains in the final submitted package; the selected beta=8,delta=3/4 local-sink example is covered by the earlier full two-node stability classification, and the local cubic law was published already. Sound exposition/corroboration cannot rescue a covered original.

The dated certificate retains the supplied scientific assessment, sources and limitations.
