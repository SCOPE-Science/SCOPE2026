---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

At each base coordinate z the two rows are independently in the span of (z²,z,1) and (2z,1,0). On the rank-two locus the derivative coefficients recover the ruling point, so this row-space model computes the degree of the actual tangent-plane incidence map. Its normal is [1:−2z:z²]. Away from characteristic two the annihilator discriminant gives H, recovering z rationally on M_0≠0. The rank-one locus cannot supply a hypersurface component and the displayed rank-two point has derivative ∂H/∂A_0=4, so H is geometrically prime in these characteristics. Along the rank-one divisor H lies in the square of its defining ideal; nonregularity in codimension one follows even over imperfect fields. In characteristic two the normals fill a dense part of the line M_1=0 geometrically, and Q is an irreducible 2-by-2 determinant. Its gradient ideal is exactly (A_0,A_2,B_0,B_2); codimension three of the singular locus and the hypersurface S_2 property give normality. On A_2=1, Q solves for B_0, and A_0 has valuation one at (A_0) in the resulting rational function field. Adjoining its square root gives the whole generic incidence field and purely inseparable degree two. Primitivity gives a torsion-free integral homogeneous-coordinate quotient and flatness, with special equation Q². This is a geometric image, not the closure of just the k-rational tangent planes. The supplied verifier and recorded output were inspected, not run; their finite samples are not needed for these arguments.

## originality

PASS

The characteristic-zero quartic case and analogous characteristic-two discriminant degenerations are established prior work. The exact matching local mirror has the same identity as the frozen record and is not independent prior evidence. The distinct related records and inspected primary literature do not supply the fixed S(2,2) reduced characteristic-two image, degree and normalization behavior together or the quartic-to-double-quadric comparison for it. This pass is limited to that characteristic-dependent result and not the characteristic-zero equation by itself.

## value

PASS

The balanced quartic scroll is a basic, fixed embedded test case for tangent schemes in mixed characteristic. The exact comparison separates three phenomena that an equation over characteristic zero alone misses: noncommutation with reduced image, the change in normality, and inseparable generic incidence despite a single geometric generic preimage. These are useful model-specific boundary data, not merely a modular polynomial expansion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
