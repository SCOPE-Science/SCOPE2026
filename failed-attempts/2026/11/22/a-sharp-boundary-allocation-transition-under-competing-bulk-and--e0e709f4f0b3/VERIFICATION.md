---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Solving the backward equation in the dimensionless coordinate gives Φ=A cosh(kz)+a(A−1)sinh(kz) with A=(aC+b+abS)/(S+KC+abS). The two Robin conditions and hyperbolic addition recover the submitted closed form, with positive denominator. Write u=k(1−z), t=kz, U=cosh u, V=cosh t and H=sinh u+sinh t. Differentiating in a with b=K−a gives P(a)=δSa²−2Za+KZ+δd₀ with δ=U−V, d₀=S+KC, Z=Hd₀−SKV. For z<1/2, B₂=(C−1)sinh t≥0, giving Z−δSK=SH+KB₂>0, so P is strictly decreasing over the whole budget interval. Its midpoint sign is positive, and P(K)=δS−B₁K−B₂K² decreases strictly from positive to negative as K grows. This yields the positive unique threshold, includes equality at the boundary optimum, and gives the left-wall threshold K_c=S. At the midpoint δ=0 and Z>0, giving the unique balanced split; reflection treats the other half. Replay: RESULT.md, Exact transform, Optimality derivative and Threshold and classifications. The uploaded checker was inspected, not executed. This assesses correctness of the capture formula and mathematical classification; the separate frozen assertion that the resetting theorem cannot yield them is contradicted below.

## originality

FAIL

The earlier two-trap resetting record already solves a positive-rescaling-equivalent allocation problem. The reduction preserves the entire fixed-budget objective as a function of the allocated share, not just one critical sign. The frozen claim that no such specialization or reduction exists is false.

## value

FAIL

The physical question and the contrast with minimizing ordinary mean reaction time are useful. As submitted, however, the claimed structural novelty is an exact reparameterization of the earlier probability allocation, not an independently new boundary or invariant; the single wall-start formula is a direct edge specialization of that same law. No separate valuable mathematical remainder was established for repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
