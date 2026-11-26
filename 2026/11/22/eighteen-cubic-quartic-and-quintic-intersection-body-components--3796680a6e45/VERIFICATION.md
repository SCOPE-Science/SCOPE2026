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

The vertex mean is the interior origin, the base heights are p-z, -q-z, -p-z, q-z, and the apex height is 4z. Thus the two open half-spaces each have nine sign chambers. I reconstructed all eighteen homogeneous radial functions by a different exact method: intersect the crossed original edges with u-perp, order them by face adjacency, and divide the signed z component of the polygon's vector area by z. Its absolute value is area/||u||, with orientation fixed on each chamber. Exact symbolic reduction matches all 18 certificate profiles and witness signs, verifies coprimality and all 153 pairwise distinctions, and gives denominator degrees 3/4/5 with multiplicities 8/2/8 respectively; the horizontal section has area 64/25. The proof's coarea normalization and tetrahedron volumes 10/3 give the factor 10 independently. Coprimality over Q gives coprimality over C (the common-factor locus also descends); the homogenization D-10wN is primitive linear in w and irreducible, and dehomogenizing preserves irreducibility here. Comparing the two homogeneous pieces rules out coincident components. On z=+/-1 the rational radial map of a sector into its hypersurface has the projection from the origin as a rational inverse on the patch. The sector is open in the real chart and hence Zariski dense in the complex chart, so the patch is dense in its irreducible hypersurface. Continuity makes all wall directions limits of these patches, so the closed union gains no component. This proves total degree 72 and absence of linear components. For an invertible A, coarea or the planar area Jacobian gives rho_{AP}(u)=|det A| rho_P(A^T u), so the linear-image assertion follows by the invertible map |det A| A^(-T) on the boundaries.

## originality

PASS

The prior general chamber and rational radial-function algorithm applies, and the novelty is not the method, affine covariance, or existence of a degree bound. For this five-vertex pyramid the published bound is six; it gives neither the actual top degree five, the lower-degree components, nor the distinctions of branches after reduction. The exact distribution requires the pyramid-specific symbolic cancellation and chamber comparison. The strongest related same-pyramid findings read concern section probabilities or a different center rather than algebraic boundary. The identical indexed hit is the target itself.

## value

PASS

The vertex-centered square pyramid is a canonical minimal non-tetrahedral three-dimensional polytope; exact algebraic boundary degrees are a natural test of the gap between chamber combinatorics and boundary algebra. This case exhibits three different nonlinear degrees rather than the two in the known tetrahedral example, improves the attainable maximum for this body from the general upper bound six to five, and shows explicitly that equal quadrilateral section size need not give equal algebraic component degree. The precise degree multiset and chart rule are useful benchmarks for intersection-body algorithms, not just a renormalization of a known example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
