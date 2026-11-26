---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The constraints imply 4w<a and 0<L−w≤L+w<2P for every admissible P. Each window can contain at most one center; only one-period transit pairs can contribute. The possible first-center times are [0,w]∩[L−P,L−P+w], of length (w−|L−P|)_+; divide by P and integrate against π. Dominated differentiation gives the clipped right mass minus the clipped left mass. For decreasing h, on the full-support interval the right mass is smaller by pointwise translated comparison. For b−w≤L≤b it is still strictly smaller: the right interval is shorter than or equal to the left, and compared to the same-length initial part of the left interval its integrand is smaller (at L=b the right mass is zero). This fills a sign step omitted from the frozen proof. At the left edge the derivative decreases strictly, with slope h(L+w)−2h(L)<0 and opposite signs at a and a+w; beyond [a,b] the signs point inward. Reflection proves the increasing case. Constant h gives equality precisely on [a+w,b−w], possibly a singleton. Integrating 1/P and P in the edge equations gives the two stated quadratics; substituting (3,4,0.2) independently gives 3.188194301613414 and 3.809987531152684. The theorem is exact in the model, not an empirical calibration. The supporting SLOGAN overstates discontinuity: that description of the power-law optimal lag requires b>a+2w; the actual Finding does not assert a jump when the plateau is a singleton.

## originality

PASS

What survives comparison is the sharp lag design law for a period prior and ideal separated, equal windows, not the familiar phase-window function or the triangular overlap identity. The strongest inspected source for period-prior weighting uses fixed baselines; the strongest indexed transit-center alias comparison varies orbital period at a fixed daily schedule. Neither yields the edge placement, exact neutral plateau or the critical exponent for the lag optimization.

## value

PASS

The physically motivated design question asks whether a sparse follow-up should target the middle of the uncertain-period range or one edge. The theorem gives a sharp answer, including an exact flat regime, and supplies boundary equations and closed-form test cases for survey-cadence calculations. The useful invariant is the optimizer of the physically reweighted prior, not another statement of cumulative transit probability. Its benchmark value does not depend on realism outside the stated idealization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
