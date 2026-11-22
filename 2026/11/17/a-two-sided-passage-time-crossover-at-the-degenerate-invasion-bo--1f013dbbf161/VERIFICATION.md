---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Reconstructed exact fast-slow variables s=1-x,z=s-y, with fast eigenvalue -a and center variable y. Exact Taylor expansion near E=(1,0) gives center graph z=gamma*y²+(b/a)delta*y+O_3, gamma=(1+aq)/a>0, and reduced drift by(gamma*y²-delta)+ controlled terms. Independent symbolic elimination of the positive equilibrium nullcline recovers y*=gamma^-1/2 sqrt(delta)-(a+2)/(2(1+aq))delta+..., the x* coefficient, and the boundary eigenvalues -a,-b delta. Rescale delta=±epsilon, y=sqrt(epsilon)Y, tau=epsilon*t to scalar bY(gamma Y²∓1), integrate finite blow-up times to exact logarithms, use bounded K-cutoff positive cubic drift and strong-stable foliation to reach fixed eta; for delta>0 below critical amplitude E is attracting, at delta=0 time is y0^-2/(2b gamma). Critical amplitude Y0=gamma^-1/2 excluded. Algebraic checker supports coefficients; singular infinite-time claims depend on analytic comparison.

## originality

PASS

Best-of-knowledge PASS for model-specific full 2D two-sided fixed-section passage theorem and exact amplitude threshold. Chen et al 2023 already identify this degeneracy and its nonhyperbolic saddle type, and generic cubic normal form/pitchfork slowing is prior; no inspected theorem provides these precise starting-data passage laws across c=1 in this original Allee–fear system.

## value

PASS

Quantified invasion bottlenecks at a naturally degenerate ecological competition boundary are meaningful dynamics beyond a qualitative stability chart: the theorem gives exact log passage profiles for either detuning sign, a nontrivial initial-amplitude survival/extinction threshold and a critical inverse-square timing coefficient from physical 2D initial conditions. These are useful model-specific invariants requiring fast-fiber and fixed-height estimates, not just a textbook center-manifold designation. No global ecology or equality-layer claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
