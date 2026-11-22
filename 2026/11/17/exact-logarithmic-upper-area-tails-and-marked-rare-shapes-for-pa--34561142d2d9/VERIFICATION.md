---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

PASS. Re-derived affine square coordinates with four side-selection masses u,v,u,v (arclength matters), where u+v=1/2. Exhaustive occupancy weights for three distinct, two opposed, two adjacent and three coincident sides are 6uv,6(u^3+v^3),6uv,2(u^3+v^3). The distinct-side deficit W=x(1-y)+yz gives a piecewise truncated triangle integral F(eps); opposite sides give eps^2; adjacent give J(eps). Algebra gives the claimed .75 eps^2+6uv H(eps) for each 0<eps<.5, with positive H series starting eps^2 log and strictly positive k>=4 coefficients. The maximum is S/2 and rhombi maximize uv. For y in [eps,1-eps], change X=x(1-y)/eps,Z=yz/eps has an exact simplex Jacobian eps^2/[y(1-y)]; normalized simplex Dirichlet(1,1,1) and logarithmic y-density imply joint total-variation mark convergence; outside mass O(eps^2) vs leading eps^2 log. Independent direct numerical analytic integrals/mixture algebra at eps=.03,.1,.2,.49 agree. Angle independence and fixed-positive-sides caveat observed.

## originality

PASS

PASS, bounded: 2026-11-02 all-parallelogram boundary-sampled expected convex-hull area theorem has same arclength masses and rhombus shape ordering but an expectation does not determine the high-area event distribution for exactly three points, especially logarithmic correction and joint conditional Dirichlet marks. Area-uniform interior square triangle papers sample a different measure and have a different exponent. Related circular random polygons and 4-point one-side-each quadrilaterals are different random objects. No exact three-boundary-point tail / same conditional law located in direct corpus searches.

## value

PASS

PASS. The logarithmic boundary rare-event singularity, universal nonlog quadratic coefficient, strict all-threshold rhombus ordering and exact independent logarithmic/Dirichlet rare-shape marks provide a nontrivial probability classification for a natural geometric sampling scheme, not a restatement of expected-area extremality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
