---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Torus tangency is exactly Ax=0 at a torus vector. For each rank bound r>=3, the Gram map from n copies of the irreducible isotropic cone in k^r surjects onto the hollow rank locus. Isotropic vectors span k^r, so generically all r-column minors are nonzero; for r=n-1 this gives full-support kernels, proving density of tangencies. The derivative 2 adj(A)_ij is nonzero for some pair at these points, so the determinant is reduced. At corank one all derivatives vanish exactly when the generator of the kernel is a coordinate vector. At higher corank the adjugate is zero. The rank-(n-2) Gram locus has dimension n(r-1)-r(r-1)/2=N-3 affinely, by the full-rank orthogonal orbits. It has points without any zero row; each zero-row component has a corank-one point given by an all-ones hollow complementary block. Their dimensions and distinctness give precisely n+1 projective components. Independent check of transversality without witness computation: the dual of restriction of hollow variations to K=ker A has kernel precisely the symmetric tensors on K whose ambient image is a diagonal matrix. A nonzero such diagonal matrix has a coordinate vector in its image and hence in K, impossible away from the zero-row loci. The restriction is therefore onto, and the three Schur-complement entries are independent normal coordinates with equation uv-w^2. Along a generic zero row, the exact Schur complement is minus v^T B^(-1)v times a unit, nondegenerate in n-1 normal coordinates. These are also projective local assertions since radial variation restricts to zero on the kernel. Hypersurface S2 together with codimension >=2 of the singular set gives normality; n>=5 gives unequal codimensions. No Jacobian-scheme decomposition is inferred. The frozen title and body both say n+1; the directory slug is not a mathematical assertion.

## originality

FAIL

The dual equation is already covered by published second-hypersimplex discriminant work; a separate indexed Resultary finding gives exactly the asserted n+1 hollow determinant components and the two precise generic transverse types, over a broader characteristic range. Together they cover the substantive mathematical claim. The same displayed date of the duplicate singularity result does not determine priority or imply that the two proofs have the same provenance.

## value

FAIL

The dimension jump and two different transverse models are meaningful facts about a natural discriminant. However, both models and the singular-component decomposition are available for the same hypersurface, and the toric-dual identification is already encoded by the full-support discriminant. The frozen work adds no new singular stratum, scheme structure or independent result beyond those covered facts and their dimension and normality consequences.

The dated certificate retains the supplied scientific assessment, sources and limitations.
