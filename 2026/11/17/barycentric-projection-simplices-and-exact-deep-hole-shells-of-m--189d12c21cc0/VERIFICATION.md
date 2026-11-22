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

The residual from the missing vertex (e_i,e_j) to the equal-weight average of 2(q+1) permitted edges has row coefficient +1/2 at i and −1/[2(q+1)] at j/outside, and analogous column coefficients. Direct checking of all permitted generators places exactly those 2(q+1) active edges on the supporting hyperplane and every other generator strictly below. The two disjoint-star incidence columns form a forest, hence their convex hull is a simplex of affine dimension 2q+1, not a lower-rank face. The projection normal inequality gives unique closest point, squared norm (q+2)/[2(q+1)], and the exact edge Gram determinant 2(q+1)(q+2) yields the simplex volume. Each missing ordered pair contributes to the size-specific distance shell; q=n−part_size and monotonicity of the rational function select only maximum parts. For any nonvertex point of the full product Q, residual averaging together with strictly distinct residual vectors makes the squared distance strictly lower, proving the full continuous Hausdorff maximizer classification. Independently assembled incidence matrices for q=1,2,3,4 and checked squared distances .75, 2/3, 5/8, 3/5, and Gram determinants 12,24,40,60.

## originality

PASS

The exact PQ-type multipartite graph family is studied by Ohsugi–Tsuchiya, whose actual primary full text yields Ehrhart/h* and normalized volumes, not intrinsic Euclidean metric projection. A published biclique-deletion metric theorem and crown matching special case overlap some geometric constructions but do not state or dominate the multipartite off-diagonal removal shells and face dimensions for arbitrary part sizes.

## value

PASS

A natural and well-studied family of PQ adjacency polytopes is compared with its containing product of simplices. Exact Euclidean nearest-point simplices, their intrinsic volumes, every discrete distance shell, and the full continuous Hausdorff extremizer list give motivated sharp geometric invariants, useful beyond the existing Ehrhart computations. The arbitrary-class-size classification is not an arbitrary small instance or a parameter renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
