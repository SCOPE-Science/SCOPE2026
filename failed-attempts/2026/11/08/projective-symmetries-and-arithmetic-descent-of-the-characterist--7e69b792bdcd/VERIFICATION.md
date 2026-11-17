---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

The singularity calculation F_X=Z^(q+1), F_Y=0, F_Z=X Z^q fixes P=[0:1:0] and its tangent Z=0. The affine curve is isomorphic to A¹ via (x,y)=(t^q,t^(q+2)+t) with a polynomial inverse. Any projectivity fixes P and the tangent and induces t↦αt+β. Comparing coefficients of 0,1,2,q,q+2 in the transformed affine parametrization for q>=4 forces β=0, α^(q+1)=1 and the full diagonal family diag(α^q,α,1). Intersecting μ_(q+1) with F_(2^r)^× gives gcd(2^n+1,2^r−1); order_(2^n+1)(2)=2n since 2^n≡−1 and every proper divisor of 2n is ≤n. Arithmetic order independently checked for 2≤n≤24. This correctly classifies geometric points, not stabilizer group schemes.

## originality

FAIL

Decisively covered by full prior results: October 12, 2026 published theorem on non-smooth projective stabilizers proves the identical geometric group for all n≥2 (indeed extends to n=1) and further computes reduced group and 3-dimensional infinitesimal tangent; October 25 full published theorem independently gives the exact same diagonal geometric stabilizer and coefficient-comparison proof. The submitted finite-field rational stabilizer count and smallest defining field are immediate cyclic-group intersection and elementary multiplicative-order consequences of the earlier explicit matrices. No nontrivial original mathematical remainder; reject despite correct proof.

## value

PASS

The full embedded-curve projective symmetry and arithmetic field-of-definition profile is a natural geometric/arithmetic invariant, structurally different from arbitrary automorphisms of its normalization. It is worthwhile mathematics, but the complete invariant follows from the published explicit projective stabilizer; this V assessment does not rescue the originality failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
