---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

The integer-oversampling q=2 Zak multiplier has the scale L=1/b=2a and equals L(|Z_L g(x,theta)|^2+|Z_Lg(x+a,theta)|^2). For 1/4<b<=1/2 there are no aliased tent replicas, and exact one-dimensional convexity gives A=a(2-a)^2 and B=2a; when b<=1/4 the essential lower bound vanishes. For 1/2<=b<=3/4, d=1-a ranges 0..1/3; explicit finite tent sums yield the two channel formulas in RESULT.md. The phase extrema occur at 0/pi because active coefficients are nonnegative; each x-piece is quadratic and its critical/endpoints give A=2(1-d)min((1+d)^2/2,4/5), B=2(1-d)(1+4d^2). Independently symbolically differentiated these exact branches: kappa=B/A has unique minimum 8/5 at d=1/4, B has unique minimum 50/27 at d=1/6, and A maximizes at d=sqrt(8/5)-1, distinct optima. At b=1/2 formulas agree with A=1 B=2, and b=3/4 endpoints satisfy alias-scope assumptions.

## originality

PASS

Best-of-knowledge: the first-alias b<=3/4 exact quantitative bounds and triple distinct lattice optimization do not follow from qualitative hat-spline frame-set theorems or the published b>=1/b>=3/2 cases. An inaccessible full text of two highly relevant 2026 spline papers remains a specific residual risk rather than an automatic failure.

## value

PASS

A natural q=2 Gabor stability design problem asks whether minimizing spectral condition ratio, minimizing upper bound and maximizing lower bound select the same rectangular lattice. The exact first-alias analysis proves three different uniquely optimizing lattice shapes, with sharp constants. This is a motivated spectral optimization result rather than a parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
