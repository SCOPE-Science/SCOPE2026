---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Three distinct nodes are unisolvent for degree two, and the known Gaussian flat-limit theorem applies (positive target variance is handled by rescaling). Independently, removing the factors exp(-h x_i²) from the kernel system and taking Vandermonde coefficient combinations of its rows, divided by (2h)^k/k! for k=0,1,2, gives the ordinary moment system in the limit by Taylor expansion and Gaussian integrability. The signs of the Lagrange denominators are +,-,+ in sorted order. For one negative node -u and two positives, strict positivity means precisely that the positives straddle q/u; reflection and labeling supply the factor 12. Weight-zero events have measure zero. On the log scale the probability is 3/2 times g*(F(1-F)). Strict decrease of the log-density derivative gives strict decrease of the reverse hazard and strict increase of the hazard, hence strict log-concavity of both factors. In the one-dimensional Prékopa–Leindler transport proof, the strict factor inequalities cannot both be equalities when the convolution arguments differ: they would require v0=v1 and t0−v0=t1−v1. This gives a strictly log-concave convolution. Dominated convergence gives zero at both ends in q; differentiation on compact positive q intervals is justified by Gaussian tails and gives the unique critical point. At large h, the relative corrections to the strictly positive order-h^(-1/2) kernel means vanish for each fixed distinct node triple. Bounded convergence then gives both probability endpoints.

## originality

PASS

The supported distinction is the Gaussian three-node quadratic positivity probability as a function of proposal scale and the proof of a unique optimum. Neither the flat Gaussian reduction nor the general positivity-feasibility setup is new. No inspected distinct record or prior theorem gives the Gaussian probability and scale optimization.

## value

PASS

This is a motivated exact baseline for when an unaugmented Gaussian kernel rule can lose weight positivity in the flat limit. The strict scale optimum shows that matching the target is suboptimal, but even the best Gaussian proposal remains positive only about one quarter of the time. This is a benchmark about weight signs, not accuracy, optimal finite bandwidth, or arbitrary proposals.

The dated certificate retains the supplied scientific assessment, sources and limitations.
