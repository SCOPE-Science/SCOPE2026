---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

At Pareto α in (0,1), λ>0, ε_n=(λ/n)^(1/α), the rescaled weights ε_n W_i form a PPP with intensity λα t^(-1-α)dt. For fixed hub threshold δ>0, any two hubs are deterministically adjacent for large n; a uniformly selected root with W<=M has expected lower-hub neighbors at most λαM δ^(1-α)/(1-α), yielding a vanishing fraction of nonclique neighborhoods by taking δ↓0 then M↑infty. For fixed δ, conditional independent nonhub-to-hub edge indicators plus bounded variance give empirical fraction degree>=2, yielding the claimed random PPP functional Q by converging-together. Poisson thinning gives H_w~Poi(λw^α/(1-α)) marginally, and the exact Pareto integral gives E Q=1-exp(-λ/(1-α)). The event N=Π([1,infty))>=2 forces Q=1; if N<=1, an interval of root weights w≈1 has positive chance of H_w<=1 because remaining success parameters are summable, forcing Q<1. Thus P(Q=1)=1-e^-λ(1+λ). Finite numerical integration checker tests identities but not distributional convergence; main analytic proof supplies latter.

## originality

PASS

PASS best-of-knowledge after material full-text comparison. Andreis–Avena–Hazra–Matteini (arXiv:2610.29564v1) treat exactly the same hard-capped Pareto critical rank-one graph. Their FULL accessible arXiv HTML was inspected (model Section 1.1, Theorems 1–6, the Poisson environment and giant-component proof in Section 3, connectivity in Section 4, discussion, appendix): their explicit results concern degree, giant size, connectivity, component size and maximum degree, not an empirical local-clustering limit nor its perfect-clustering unit atom. Their discussion attributes earlier clustering non-self-averaging to a distinct exponential soft kernel. Catanzaro–van der Hofstad–Garlaschelli prove local clustering for that soft kernel with p=1-exp(-epsilon W_iW_j), whereas the hard-cap model gives certain hub-hub edges and an atom absent in the soft model. The novelty is the exact empirical local clustering functional, its expectation and unit atom, not any general PPP, degree limit or lack-of-self-averaging mechanism. Residual older literature priority risk remains.

## value

PASS

Perfect local clustering probability for the vertex-averaged statistic is a natural, exact distributional feature of a critical infinite-mean random graph. Hard edge saturation creates deterministic two-hub cliques and a nonzero perfect-clustering atom that distinguishes it sharply from otherwise similar exponential-kernel clustering. The exact atom and expectation are motivated model-discriminating invariants beyond mere generic heavy-tail non-self-averaging.

The dated certificate retains the supplied scientific assessment, sources and limitations.
