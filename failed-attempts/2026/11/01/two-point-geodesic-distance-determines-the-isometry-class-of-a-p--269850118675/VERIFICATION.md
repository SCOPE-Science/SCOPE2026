---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For every full-rank planar Euclidean lattice, the difference of two independent Haar-uniform torus points is Haar, and choosing the Voronoi representative yields F(r)=area(V∩B_r)/det Lambda. The local r→0 limit recovers det Lambda. Polar differentiation yields angular exclusion H(r)=2π−det(Lambda)F'(r)/r. For each strictly interior Voronoi facet foot at h=||v||/2, newly excluded arcs of length 2 arccos(h/r) produce a noncancellable 2m(h)sqrt(2/h)*sqrt(r-h)+O(r-h) onset; pre-existing active arc boundaries are locally Lipschitz even at vertex coincidences. Thus the multiset of 4 or 6 facets and their distances is recovered, giving rectangular generator lengths or obtuse-superbase lengths and the Gram matrix. All equal-length degeneracies are handled. Independent numerical checks of square-root singularity coefficients on rectangular and hexagonal Voronoi cells; universality rests on exact geometry and known 2D Voronoi-relevant-vector theorem. The main rigidity conclusion is independently known, however, which affects O, not this C result.

## originality

FAIL

DIRECT PRIOR COVERAGE: Mémoli and Needham, arXiv:1810.09646v3 §5 Flat Tori, Proposition 5.16 (2021 preprint, published 2022 doi:10.1111/sapm.12526), already prove: two R²/lattice flat tori have the same global distance distribution iff their aligned lattice point sets agree. In their homogeneous tori the global law is exactly the two-independent-Haar-point intrinsic geodesic-distance law of this claim. Equality of lattice point sets after rigid alignment gives isometric flat tori; conversely isometries preserve the law. The present headline theorem is thus explicitly proved years earlier. Their proof uses volume growth and critical radii, while the submitted proof uses facet-foot square-root onsets; a different proof or an unclaimed detailed cusp mechanism is not originality for the same final isometry-rigidity claim. No viable complete new RESULT.md/SLOGAN.txt rewriting and full reassessment were prepared; reject original, do not relabel as repaired.

## value

PASS

The geometric reconstruction via square-root angular cusps is mathematically motivated and may furnish a useful alternate constructive route to the natural distance-law inverse problem. It is a substantive full-moduli rigidity fact rather than a tiny experiment. Nevertheless the actual headline is previously established; this intrinsic interest does not rescue failed originality or authorize acceptance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
