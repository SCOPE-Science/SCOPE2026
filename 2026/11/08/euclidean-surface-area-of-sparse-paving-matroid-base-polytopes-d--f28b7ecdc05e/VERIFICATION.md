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

For 2<=r<=n-2 with connected sparse paving M, the canonical polytope is the rank-r hypersimplex with each circuit-hyperplane corner cut by x(H)<=r-1. Hypersimplex coordinate facets have Eulerian-number Euclidean volumes. The removed corner has new facet Delta(r,r-1) x Delta(n-r,1) of (n-2)-volume sqrt(r(n-r))/((r-1)!(n-r-1)!) and old facet losses r L_1+(n-r)L_0. Distinct circuit hyperplanes overlap in at most r-2 elements, so their strict removed corners and positive-area cut patches have disjoint relative interiors. Summing produces A=A_0-lambda D. D is strictly positive and symmetric; comparison of factorial denominators and the displayed inequalities proves strict increase toward middle rank. Verified n=5,6,7 Euclidean convex hulls independently in an orthonormal affine basis and coefficient inequalities for n=4..34, including the n=6 r=3 two-intersection-pattern example; these finite tests do not replace the all-n proof. Lower-dimensional disconnected exceptional cases are excluded.

## originality

PASS

PASS with a substantial and explicit prior-coverage restriction. Ferroni and Schroeter (2024) Corollary 5.4 ALREADY proves that every valuative matroid invariant of sparse-paving matroids depends only on n,r and number of circuit-hyperplanes, hence already covers this invariance for the surface-area intrinsic volume. The surviving result is the *evaluated ordinary Euclidean* coefficient D(n,r) with its metric covolume factors, strict positivity and exact rankwise balanced extremum; those numerical/ordering assertions were not found in the relevant Corollary 5.4 or the face-vector paper. Do not credit circuit-hyperplane-count invariance as new.

## value

PASS

Ordinary Euclidean boundary area is a natural metric invariant distinct from lattice-normalized Ehrhart boundary coefficients; evaluating its exact corner loss and proving rank optimization provides a reusable quantitative fact. Its geometric metric weight requires actual facet-angle/volume analysis beyond simply invoking the earlier valuation formula. The independence assertion alone, being known, is NOT the basis for value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
