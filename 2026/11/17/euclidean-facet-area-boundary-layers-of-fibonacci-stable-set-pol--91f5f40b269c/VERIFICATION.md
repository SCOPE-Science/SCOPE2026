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

PASS. Reflecting even coordinates is an isometry between P_n of path stable sets in unscaled R^n and the zigzag order polytope, so Euler zigzag volume E_n/n! is an admitted antecedent. Exact slicing separates independent subpaths: coordinate area a_{j-1} a_{n-j}; edge area sqrt2 times integral A_{j-1}(1-t)A_{n-j-1}(t) with A'_r(t)=A_{r-1}(1-t). The generating function solves F_tt=-z²F, F(z,0)=1 and reflection derivative, giving F(z,t)=cos(zt)+tan(pi/4+z/2)sin(zt). Its isolated nearest simple pole z=pi/2 has leading coefficient (4/pi)(2/pi)^r sin(pi t/2) uniformly in t, with O(pi^{-r}) remainder after analytic subtraction on |z|=pi; fixed-index and both-tail-diverging index limits follow, including distinct endpoints. The divergence theorem with fields x and x-(1/2)1 yields sum of coordinate facets 2n*volume and edge facets sqrt2*n*volume. Independently regenerated rational recurrences and integrated each labelled facet for n=2..18; both aggregate identities held exactly, and n=18 ratios C1/V=1.5707963322 and C2/V=2.4674010833 match pi/2 and pi²/4. Prior universal area total alone and short finite enumeration do not establish all indexed asymptotics. No sharp all-index maxima is asserted.

## originality

PASS

Best-of-knowledge PASS for explicitly indexed boundary facet formulas and especially endpoint-to-bulk asymptotic transitions; total surface/volume identity and generic contracted-poset facet area formula are prior and not independent novelty.

## value

PASS

PASS: Every position-dependent Euclidean boundary facet area is a natural boundary statistic of a canonical Fibonacci/zigzag polytope; a uniform nearest-pole argument reveals explicit endpoint anomalies and a universal bulk even when indices diverge arbitrarily slowly. It is a genuine geometric asymptotic refinement beyond the known global area/volume flux relation. The latter and generic finite area computability alone are not counted as new value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
