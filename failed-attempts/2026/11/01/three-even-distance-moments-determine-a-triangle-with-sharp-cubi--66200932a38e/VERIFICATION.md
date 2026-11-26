---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Independently integrated on the barycentric difference domain: in two coordinates the overlap density of the difference w with sum w_i=0 is 2(1−sum max(w_i,0))² on sum max(w_i,0)≤1. In each of the six sign sectors the square-distance polynomial is x u²+y v²+(x+y−z)uv for the two incident sides x,y at the isolated-sign vertex and the opposite side z; the Jacobian is one. The beta integral of u^p v^q(1−u−v)² over u,v≥0, u+v≤1 is 2p!q!/(p+q+4)!. The exact independent replay (python3 /workspace/branches/independent_triangle.py) gives coefficients 1/18 and 1/60 on pure degree-one and degree-two monomials, zero mixed degree-two coefficient, and coefficients 23/4200, 7/4200, −28/4200 on the cubic pure, mixed squared-linear, and xyz patterns respectively. The inverse elementary symmetric formula and side-side-side congruence establish injectivity. The two explicit triangles are strict for the stated small r, share m1 and m2, have |Δm3|=r³/420 and ordered squared-side discrepancy r. For the uniform bound the coefficients are Lipschitz in the bounded input moments, so on the boundary of any cluster of radius-η disks about the first roots the original polynomial modulus is at least η³; choose η comparable to δ^(1/3), with a generic slightly larger radius if disks are tangent. Rouché preserves multiplicity in each cluster, with diameter at most 6η; a real matching bounds ordered discrepancies as well. At δ=0 the cubics agree, and for large δ the root bound suffices. The example rules out all larger exponents near equilateral. The result concerns squared sides and population moments, not a sampling theorem.

## originality

FAIL

The distinct earlier record 3e3e8b4e2ad2 states all three identical moment identities, the same cubic inverse, two-moment failure even with area as an extra datum, and uniform optimal 1/3 inverse Hölder stability on squared sides bounded by 1. The general bound B in the frozen finding follows by scaling squared sides by 1/B and moments by B^(−k). Other direct matches include a distinct same-day record with additional fiber classification. None of the frozen scientific conclusions survives as a distinct contribution.

## value

FAIL

A minimal finite-moment inverse and optimal stability near a symmetric triangle are intrinsically worthwhile, but both are already present in the checked indexed work. The general size bound is a direct scaling corollary, and the alternate sharpness witness and coefficient expansion do not produce a new mathematical invariant or a better bound. No substantive remainder to repair is established in the frozen finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
