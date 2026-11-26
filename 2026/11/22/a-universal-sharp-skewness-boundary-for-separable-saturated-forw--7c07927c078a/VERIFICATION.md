---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For y=F_s x, put v=g(y) and r=y-v. Oddness and monotonicity of both f and Id-f make the sign changes and coordinate sorting putting v and r in the same 45-degree cone simultaneous. Thus r·v≥|det(r,v)|, and F_s^{-1}=(I-sJ)/(1+s²) gives x·v≥||v||²/(1+s²) when |s|≤1. Expanding the square proves sufficiency including the endpoint. At zero the derivative has squared norm 1−2γ+γ²(1+s²), proving failure above the claimed bound. For s>1 a fixed b with sf(b)>L makes (1+s²)x·v=a(f(a)−sf(b))+b(sf(a)+f(b)) negative for large a; reflection handles negative s. At y=(0,b) the second Jacobian column tends to (γs,1); for s=0 the scalar secant slopes give the pairwise result. In y-coordinates the 1-smooth potential gives the strict decrement γ(1−γ(1+s²)/2)||g(y)||². Since f is monotone and positive on positive arguments, g(y_k)→0 forces y_k→0 without a compactness assumption. No convergence at equality is asserted; an admissible response linear in a neighborhood of zero can give a nonshrinking linear orbit there. The exact s=2, γ=1/5 witness checks out. CHECK.py and VERIFICATION.md were inspected, not executed: the code tests 625 states per skew, 3,750 across six skews (the prose says per skew), for a total of 18,792 rational assertions including the separate witnesses. All tests use a single response; the proof supplies universality.

## originality

PASS

The verified distinct contribution is the two sharp Euclidean classifications for this specific planar family, not the general descent principle or the existence of a non-Fejér example. The closest actual prior example has the very same separable preconditioner and s=2 but no universal skew or stepsize classification.

## value

PASS

Resolves a concrete limitation left by a known separable example: stable trajectories can lose Euclidean Fejér monotonicity at an exact 45-degree threshold, and pairwise nonexpansiveness can fail even on the Fejér side. The saturation argument and common-coordinate angular certificate make this an all-response result, useful for separating stability guarantees in the motivating algorithm. The strict convergence bound alone would not justify acceptance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
