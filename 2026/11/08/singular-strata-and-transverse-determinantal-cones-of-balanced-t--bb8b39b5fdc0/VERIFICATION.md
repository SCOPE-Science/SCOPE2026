---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

For projection of Gr(d,E⊕F) from [∧^d F], a one-swap affine source chart has coordinates a_j,b_i,z_ij,c, with only c (the all-F Plücker coordinate) discarded. All retained maximal minors generate precisely C[a,b,z,c z]: each c term outside the discarded minor contains some z; the retained minors recover each a,b,z and c z. The rank-one relations among (z,c z) give an exact scheme-theoretic chart A^{2d−2}×D_k, k=(d−1)^2. Its vertex locus is the Segre Z_d, with Hilbert numerator 1+(k−1)t, multiplicity k. Outside the projected tangent-direction space, Plücker quadrics solve for the omitted coordinate, proving smoothness elsewhere and global normality. Independently checked every retained minor d=3 and d=4 by exact determinants; the general determinant and inverse arguments prove all d≥3, d=2 is smooth.

## originality

PASS

The earlier fully inspected d=3 projected Grassmannian result already gives P²×P², 2×4 transverse cone and multiplicity four; that overlap is acknowledged. The present uniform theorem for every d≥3 gives unbounded k=(d−1)^2 and no extra strata, not implied by one finite instance. Broader truncated Grassmannian literature may yet imply it; original primary full text was not accessible.

## value

PASS

A uniform exact singular locus and completed determinantal local ring with multiplicity growing as (d−1)^2 is a natural, substantive geometric classification of point projections of Plücker Grassmannians; it is more than a small-case recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
