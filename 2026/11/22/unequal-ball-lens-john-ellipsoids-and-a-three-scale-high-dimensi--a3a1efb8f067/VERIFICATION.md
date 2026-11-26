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

Reconstructed RESULT.md, Proof steps 1–5. In normalized axial coordinate t the squared distance to each ball center is a strictly concave quadratic. Its maximum, clipped to [-1,1], verifies each containment separately. Two actual boundary latitudes with product −1/m admit positive masses of mean zero and axial variance 1/m; transverse sign and coordinate symmetry give full covariance I/m. John's theorem therefore certifies the unrestricted optimum. For the tip branch the increasing equation in a has lower-end value <r², and the strictly decreasing validity margin R−a−mv has limiting signs given by R−r and R−mr at the overlap endpoints. Its zero, when internal, is L_c. For two latitudes the squared radii factor as (a+H)(a+Hu²) and (a+H)(a+H/(m²u²)). The continuous L(u) has endpoint values R+r and L_c; John's uniqueness forces injectivity and matches the prescriptions at u=1. With y=u² and A=g²−1, independently simplifying the scalar equation gives the rational expression in Step 5. Brackets at fixed y, y=x/m, and y=β/√m give respectively A²/(A+y), A(x+1)/(x−1), and λ²/A=1+(2/β−β/A)/√m+O(m⁻¹). This gives the three limits including the constant (2A)^(1/4). The phrase 'the smaller ball is contained' in Step 3 has its object reversed; the preceding maximum calculation proves ellipsoid-in-ball containment, as required. VERIFICATION.md and verify.py supply recorded floating-point diagnostics, not premises of this proof; the scripts were inspected, not executed.

## originality

PASS

The supported distinction is the unequal-radius inner problem in dimensions at least four, especially the fixed-radius-ratio contact-scale transition. The contact-moment method, three-dimensional unequal case and symmetric cases are not credited as new. Same-day publication order is unresolved and unnecessary to distinguish the dimensions. No inspected comparison covers the claimed higher-dimensional result; this is a bounded assessment, not proof of priority.

## value

PASS

The result determines the unrestricted maximum-volume ellipse analogue for a natural asymmetric convex body and locates a sharp change in the actual supporting contacts. The separation-dependent m^(-1/4) critical law between the order-one and m^(-1/2) regimes supplies information not provided by a generic optimizer or by the known contact identity alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
