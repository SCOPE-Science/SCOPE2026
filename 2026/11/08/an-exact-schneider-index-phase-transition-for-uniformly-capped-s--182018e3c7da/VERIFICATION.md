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

For n=d+1, d>=3 and 1/2<=t<1, the vertices of P={x>=0,sum x=1,x_i<=t} are permutations of (t,1-t,0,...). Necessity: the cap facet is a (d-1)-simplex whose centroid requires lambda>=d-1; at the global barycenter the t-coordinate requires lambda>=nt-1. Sufficiency for lambda=max(d-1,nt-1): each face boundary is covered because any (d-1)-facet point is a combination of at most d vertices and hence belongs to one vertex+lambda face translate. For z=(1+lambda)(1/n,...), direct coordinate bounds show z lies in every translated lambda P; union is star-shaped about z, while every ray to its full convex hull endpoint meets a covered boundary point, giving full coverage. At t=1 P is a simplex with c=d by sharp centroid/Caratheodory. Thus c=max(d-1,(d+1)t-1), attaining all real t and the phase switch t=d/(d+1). Exact rational center-coordinate tests for d=3..6 and several rational t corroborate only finite cases.

## originality

PASS

Compared the theorem not merely the parameter name: the earlier exact hypersimplex index covers t=1/2; classical simplex theorem covers t=1. Neither endpoint, general face restriction, nor generic finiteness criterion implies the continuous plateau and sharp t=d/(d+1) switch. Best-of-knowledge novelty survives with unindexed-priority risk.

## value

PASS

The Schneider index is a natural affine-invariant measure of when finite vertex translates convexify a polytope. This all-dimensional, all-real-cap interpolation between a scaled hypersimplex and a simplex has two independent sharp obstructions and an unexpected d-1 plateau followed by a linear regime; the continuous exact phase boundary is not a routine endpoint substitution and is a useful complete shape-parameter classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
