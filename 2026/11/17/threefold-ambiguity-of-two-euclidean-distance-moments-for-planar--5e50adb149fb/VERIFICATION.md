---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Using independent area-uniform radial density 2r/R^2 and uniform polar angles, E(D²)=R²[1-(8/9)sinc(theta/2)^2] and E(D⁴)=R⁴[5/3-(32/15)sinc(theta/2)^2+(1/2)sinc(theta)^2]. These follow by expanding (U²+V²-2UVcos delta)^2 with E(U^j)=2/(j+2). The denominator is strictly positive. Direct numerical independent endpoint evaluations yielded K(0+)=2.7, K(pi/2)=1.79339386, K(pi)=1.95970210, K(3pi/2)=1.76893970. The supplied check_sector.py uses rational Machin-series enclosures proving K(pi/2),K(3pi/2)<9/5 and K(pi)>39/20; inspected code and analytic expressions. IVT gives three distinct roots for every k in (9/5,39/20), and R=sqrt(m/F2) matches both moments for every m>0. Nonidentical angles give noncongruent two-dimensional sectors; the third (>pi) is nonconvex. Numerical finite roots are illustrative, not the proof of a continuum.

## originality

PASS

Best-of-knowledge originality: the exact claim is not mechanically implied by inspected primary or published related theorems. The prior cone theorem neither entails planar Euclidean fourth moment nor shows that one moment ratio crosses 9/5 and 39/20 at the claimed three planar-sector intervals. These follow from independently derived sinc-squared angular laws. The standard forward moment expansion alone is routine; the strict endpoint sign pattern and open convex/nonconvex inverse ambiguity are the substantive new conclusion. See explicit access and indexing risks; unsuccessful search is not proof of priority.

## value

PASS

This is a robust open family of inverse non-identifiability, not a coincidence at a single special angle. Two common low-order Euclidean distance moments fail even to distinguish convex from nonconvex sectors, a natural identifiability question for area-uniform geometric distance statistics. The exactly signed interval and independent radius adjustment make the counterexample reusable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
