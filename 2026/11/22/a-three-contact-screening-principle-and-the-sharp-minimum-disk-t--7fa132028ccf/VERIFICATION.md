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

Independently put y=f(t) on the positive half-arch and W(y)=f^{-1}(y)^2+y^2. W'(y)=2H_f(t) for 0<y<f(a), so W is convex up to the endpoints by continuity. Squared distance from (0,z) is W(y)-2zy+z^2, and convexity bounds it by the maximum of the two endpoint values; strict increase gives strict inequality at every interior y. The center of the unique compact-set minimum disk is on the axis by reflection (uniqueness follows from the squared-distance midpoint identity). The reduced maximum is max(z^2,a^2+(d-z)^2), d=f(a); the endpoints' diameter suffices for d<=a, and the crossing z=(a^2+d^2)/(2d) in (0,d) is the unique minimizer for d>a. For the catenary H' = cosh(t)(sinh(t)cosh(t)-t)/sinh(t)^2 >0. The positive root of cosh(a)-1-a is unique by strict convexity and the sign change. The excess R-a=(d-a)^2/(2d) on the upper branch and zero below gives C^1 but not C^2, with quadratic coefficient about 0.621614671612338. For the power family, H increases for 1<q<=2; for q>2 and a=1 the squared distance from (0,1) exceeds 1 by t^2-2t^q+t^{2q}>0 near zero. RESULT.md lines 39–86 suffice independently of finite diagnostics; check.py was inspected, not executed. Weak monotonicity suffices for screening, not for counting contacts.

## originality

PASS

The standard three-point disk calculation and the convex endpoint maximum principle are not novelty claims on their own. The distinct result identifies these particular supporting points uniformly for the continuous arch under an intercept hypothesis and computes the complete catenary disk/contact transition (including its onset), with a sharp counterexample in a natural power family. The strongest exact-curve comparison inspected concerns diameter, not circumradius.

## value

PASS

The continuous covering disk is an exact geometric invariant of a standard physical curve. The theorem determines a finite sample that reproduces it exactly at any span, locates where a third point becomes active, and quantifies the first change in radius, while the power-arch example shows why ordinary convexity of the graph is not enough.

The dated certificate retains the supplied scientific assessment, sources and limitations.
