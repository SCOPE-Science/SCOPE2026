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

Exact rational elimination on all 3002 square minors of M, independently of the frozen script, gave 512 negatives, 1920 zeros and 570 positives, with nonzero minors all ±1. Oxley's explicit real representation identifies this matrix as R10. The polar inequalities are |M^T y|<=1. Full-rank active normals and total unimodularity force integral vertices, so the independent rank enumeration on all 243 ternary candidates is exhaustive for vertices: 73 feasible, 12 of rank five, exactly the claimed signed vectors. With S=MM^T, independent rational arithmetic verifies AS=2I, m^T A m=1 for each of the ten columns, the signed polar covariance sum vv^T=12A and v^T S v=10 for each polar vertex. Thus the normalized 20 signed columns are unit contacts with weights 1/4 and the normalized 12 polar vertices are unit contacts with weights 5/12; both centered weighted moments are the identity. The unrestricted Löwner criterion and centered duality give the two unique ellipsoids, and every polar facet normal has dual norm giving support one at the John ellipsoid. As a second geometric check, take the six rows of U to be minus ones and the five shifts of (1,1,1,-1,-1). They sum to zero, and U^T U=6A is positive definite. The 20 distinct signed columns map to balanced six-sign vectors: for an identity column this is immediate; for a D-column, the neighboring signs of a shifted row cannot both oppose its central sign since each cyclic sign run has length at least two. All 20 balanced sign patterns occur. In the sum-zero six-space this hull is the cube section (a section vertex cannot have two coordinates unsaturated; parity rules out exactly one). Permutation symmetry and uniqueness make the two optimizers balls there, of radii sqrt(6) and sqrt(6/5), agreeing with the matrix proof. The circulant Fourier eigenvalues are 1 and 1±sqrt(5)/3 with multiplicities 1,2,2. The ratio of the two extreme semiaxes is (3+sqrt(5))/2, and det A=16/81 gives Löwner volume (8 pi^2/15)(9/4)=6 pi^2/5; dilation gives volume ratio 5^(5/2). Volume extremality also proves the sharp containment factor among arbitrary ellipsoids, not only centered ones. The Euclidean eigenvalues and coordinate lists depend on the displayed realization; the homothety factor and contact incidences/counts are affine-covariant. The frozen script was inspected but not executed.

## originality

PASS

The R10 matrix and generalized symmetric-edge-polytope construction are known, as are the symmetric John bound and its attainment in other non-cubical families. The exact R10 pair, contact classification, and its identification as the pullback of extremal balls of a centered middle hypersimplex were not supplied by the inspected prior statements. The pass is for the specific matrix and geometry of this exceptional regular-matroid object, not the general bound, the hypersimplex's elementary ball computation in standard coordinates, or the general facet theorem.

## value

PASS

R10 is a distinguished exceptional regular matroid, and its exact unrestricted shape and facet/vertex contact data give a useful geometric benchmark outside the graphic and cographic regimes. The sharp factor or Euclidean anisotropy alone would have less force; the calculation identifies the entire contact geometry of a natural object and reveals the hypersimplex symmetry responsible for it. The computation is bounded and small, but not a known table lookup or a parameter substitution in the prior inspected graphic/cographic theorems.

The dated certificate retains the supplied scientific assessment, sources and limitations.
