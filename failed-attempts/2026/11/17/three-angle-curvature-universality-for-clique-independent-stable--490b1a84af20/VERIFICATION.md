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

The canonical stable-set hull is the m-cube fiber over the c-simplex, with c+2m irredundant facets A_i,B_j,C_j. Facet-pair codimension excludes B_j∩C_j and retains AA,AB,AC,BB,BC (different),CC. The exact Dirichlet integral ∫_{sum x<=1}(1-s)^q dx=q!/(c+q)! gives volume m!/(c+m)!, Euclidean Jacobians sqrt(c),sqrt(c+1),sqrt(2c+1), six individual ridge measures and their three universal N(N−1) normalized totals. Outward-normal products 0,−1/sqrt(c+1),c/(c+1) yield angles. Independently checked the symbolic specialization against broader multipartite formulas; the inspected geometry checker uses projected convex-hull volumes for c=1,2,3,4 small examples. No partial finite test is used to prove all integers.

## originality

FAIL

A complete published theorem for all complete multipartite stable-set polytopes (November 17, exact full RESULT inspected) implies the same split-graph ridge angle classes and normalized measures for every c>=2 by the parameter substitution k=c+1, (n_1,...,n_k)=(1,...,1,m), s=c, with normalization C=m!/(N−2)!=Vol_N N(N−1). Its right total ((k²−s)/2+(k−s)sqrt(k)) reduces to ((c²+c+1)/2+sqrt(c+1)), acute c sqrt(c), and obtuse sqrt(2c+1)/2; the interior angles supplement to precisely the split exterior ones. It also yields V_{N−2} by Steiner. k=2 (c=1) is not in the published k>=3 theorem but is a straightforward boundary case with little independently original general content. Both findings have November 17 publication dates, and order within the day is not established; the broader paper itself acknowledges split as previously derived. This is a present-coverage rejection, NOT an assertion of intra-day historical priority.

## value

FAIL

Computing exact Euclidean ridge curvature for complete split graphs is a natural and useful problem in itself; nevertheless the submitted broad phenomenon and formula are subsumed by a published full multipartite curvature result. The remaining c=1 boundary is a short specialization of the same ridge/Dirichlet mechanism and does not support a distinct valuable research contribution in this final claim. This is NOT an automatic dismissal of exact invariants or finite work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
