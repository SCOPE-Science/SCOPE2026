---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

The invertible cumulative path map L sends K_{d+1}=conv(e_i-e_j) in the root hyperplane to P_a, with L^-1 x=(-x1/a1, x1/a1-x2/a2, ..., xd/ad). Supporting facets of K_n are exactly nonempty proper subset cuts sum_{i in S}z_i<=1; each equality face spans dimension d-1 because all bipartite crossing roots lie there. Mapping chosen complement pairs by indicator flips yields |u_T.x|<=1 with each nonzero T irredundant and ||u_T||^2=sum_{i in T}a_i^-2. The unique full-flip normal gives minimal facet distance and two centered contacts; ball feasibility for every T gives the entire center polytope, with codimension one from tight opposite full-flip pair and strict slack on other faces. Root vertices are interval vectors; the longest weighted interval gives exactly two farthest antipodes. Coordinate-permutation symmetry of K_n forces unique optimal John/Loewner ellipsoids to be root-space spheres; subset-normal length squared k(n-k)/n gives their constants n/F and 2. Symmetrizing an arbitrary ellipsoid B with operator convex matrix inversion proves optimal affine containment ratio sqrt(2F/n); Cauchy-Schwarz proves R/r>=d. Independent rational d=2..5 checks directly confirmed 56 facets and norms. All d>=2/a_i>0 follow analytically.

## originality

PASS

The unweighted root-polytope combinatorics and affine symmetry ellipsoids are classical, and no independent priority is claimed for them in isolation. New packaged theorem concerns the natural opposite-pair weighted staircase difference body in its ACTUAL Euclidean metric, giving every facet distance, full incenter polytope, contact collapse and Euclidean-versus-affine comparison uniformly over all positive weights. Beck et al arXiv:1211.2039 study unsigned interval-vector polytopes, not the signed difference body/inball locus. Qu–Lee arXiv:2610.35689 abstract concerns facet normals for arbitrary staircase Minkowski sums, rather than Euclidean support distance or all inball centers; its full text was inaccessible, so detailed overlap remains a significant explicit risk. Previously published weighted simplex-generator zonotope is a projected box with n(n-1) root-difference facets, not this 2^n-2-facet root polytope. Best-of-knowledge O PASS does not assert absolute historical priority.

## value

PASS

The weighted staircase simplex is canonical in triangulation geometry; its symmetric difference body is a natural invariant rather than an arbitrary slice. The exact facet-distance multiset and entire (d-1)-dimensional incenter locus despite just two tangent facets yield an unusual structural metric classification, and all weights exhibit a fixed optimal affine shape but arbitrarily bad Euclidean radius ratio. That contrast goes beyond a textbook facet count or weight substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
