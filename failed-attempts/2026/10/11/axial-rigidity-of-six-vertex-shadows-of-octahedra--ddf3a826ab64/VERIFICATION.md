---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

For invertible A and generic plane normal U, the unique linear dependence of projected opposite vectors has coefficients c=A^{-1}U. An opposite pair drops from the projected hull iff |c_i|>|c_j|+|c_k|, because the projected image lies strictly inside the diamond conv(±q_j,±q_k). These exclusive dominance chambers subdivide into four positive trihedral cones per index and their antipodes, yielding the 1/(2pi) angle sum. Substitution A=diag(1,1,lambda) gives Omega_x=2 atan((sqrt2-1)lambda/(1+h)) and Omega_z=2 atan((h-lambda)^2), h=sqrt(1+lambda^2), hence the displayed p4. Writing t=asinh(lambda), u=tanh(t/2), a=sqrt2-1, the derivative factors as (pi/4) dp4/dt=(1-u^2)(2-sqrt2)(u^2-a^2)(u^2+3+2sqrt2)/((1+a^2u^2)(1+6u^2+u^4)). Independent SymPy simplified both sides to zero identically. Since u increases through a at lambda=1, the strict minimum is unique and endpoints yield p4->1. The standard solid-angle identity and source theorem cover all positive lambda, not a finite experiment; no assertion on arbitrary nonsymmetric affine optimum. Independent high-precision values for lambda=1/10,1/2,1,2,10 also matched the triaxial formula p4=1-p6.

## originality

FAIL

Direct mathematical coverage by two complete published 2026-10-11 results. The triaxial-octahedron theorem gives p6(a,b,c)=4/pi atan(2abc/D) for ALL positive orthogonal axis lengths, and uniquely maximizes it at equal axes. Restricting to (a,b,c)=(1,1,lambda) gives the audited full p6(lambda) law and strict lambda=1 optimum, including all lambda>0. Independently, the rectangular-box central-section hexagon theorem gives a complete all-side-length probability formula and the same rigid maximum. Polarity identifies the octahedron shadow with the polar of the central section of the reciprocal-axis box [−1,1]x[−1,1]x[−1/lambda,1/lambda] in the same projection plane, preserving 4/6 face counts. These are substantive prior mathematical implications, not merely similar titles. Both records are dated 2026-10-11, as is the assigned source, so this is a mathematical non-originality assessment and does NOT assert chronological priority, authorship, derivation, or copying. The auxiliary all-affine twelve-cone identity is expressly a proof device, a direct generic angle partition, and not a surviving separately motivated main novelty claim.

## value

PASS

Shape-dependent silhouette complexity is a motivated geometric probability invariant. An exact entire axial deformation profile and unique regular-case optimizer provide nontrivial information beyond the isolated regular-octahedron probability; both extreme deformations force quadrilateral shadows. The result is scientifically useful as a precise, naturally parameterized geometric benchmark even though the same theorem is mathematically covered by stronger published results. Value does not establish originality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
