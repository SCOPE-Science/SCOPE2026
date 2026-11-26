---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The claimed census holds over C. From the support parametrization, in z=e^(i theta) and coordinates A=x+iy, B=x-iy, the homogeneous numerators are A=-iz^8+8z^5-2iz^2, B=2iz^6+8z^3+i, Z=z^4, of degree eight after homogenization. No base point occurs at z=0 or infinity (the respective B and A coordinates are nonzero); elsewhere Z is nonzero. An independent exact Gaussian-integer substitution into the implicit invariant polynomial (q=AB, 2w=(B^3-A^3)/i) gave zero in every coefficient. The generic tangent is (-sin theta,cos theta); a second generic preimage with the same slope would be antipodal, but antipodal support points differ by 16 times the unit normal. Thus the map is birational, with image an irreducible octic, and is the P^1 normalization. At theta=pi/2, h+h'' vanishes to order two, giving coordinate orders 3 and 4 and their two rotated copies. On the axis use v=sin theta: x=8 cos(theta)(1-v^3), y=-3+8v+12v^2-8v^4. The two roots of v^2+v+1 give y=-3+12v^2=-9±6i√3; the two signs of the nonzero cosine give regular branches of opposite nonzero slope. Rotation gives six distinct nodes because the nonzero points on one axis do not lie on either rotated axis. At z=0, U=A/B=-2z^2-24iz^5+O(z^8); Z/B+iU^2/4 has leading term -16z^7. These orders certify (2,7) at [1:i:0], and conjugation gives the other one. The local contributions are at least 3×3+6×1+2×3=21, the entire genus-delta budget, so there can be no further branches or singularities. The bundled verifier was inspected, not executed.

## originality

FAIL

A distinct indexed Resultary/SCOPE record states the same complete projective singularity census, with matching curve, normalization, types, reality and coordinates. This is demonstrable equivalent coverage, not an inference of date order or of who first obtained the result.

## value

FAIL

The precise singularities of this minimal-degree example are natural and useful. But the submission gives the same already recorded invariant, with no additional singularities, geometric consequence, or general classification. Recomputing the same invariant via the half-angle coordinate does not add a distinct scientific contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
