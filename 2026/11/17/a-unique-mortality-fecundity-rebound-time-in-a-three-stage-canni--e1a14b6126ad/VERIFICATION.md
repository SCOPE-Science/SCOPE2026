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

# Reproducibility and limits

Run `python3 verify.py` using Python 3.9 or newer (standard library only). It checks twelve exact rational Laplace-resolvent equalities on three independent positive parameter triples, rational equilibrium/curvature/steady-state identities, a limiting crossing \(t_*\approx1.61615021783\) computed from the closed exponential convolution for \(c=m=\kappa=1\), and nonlinear RK4 trajectories for positive mortality–fecundity increments \(0.001,0.01,0.02,0.1\). All checks were executed successfully from the packaged file.

Exact algebra in the checker is supporting evidence only. Its finite rational tests cannot prove symbolic identities for all reals; the matrix identity in the proof does. RK4 cannot establish one crossing on an infinite time interval or for every small shock; the positive-convolution monotonicity lemma and hyperbolic perturbation argument establish those assertions. The numerical limiting crossing is illustrative, not a rigorously rounded interval certificate. The scientific claim is confined to the strict wedge, sufficiently small shocks, and the starting positive equilibrium.
