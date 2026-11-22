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

On an orthogonal quotient torus the minimizing coordinate displacement (X,Y) is uniform in the centered unit square independently of the starting phase U=(qx0−py0) mod1, which is Haar-uniform because gcd(p,q)=1. An interior transverse intersection is exactly a crossing of an integer by U+t(qX−pY), hence N=|floor(U+qX−pY)|. Conditional on W=|qX−pY|, N=floor(W)+Bernoulli({W}), whose convolution trapezoid density yields a rational piecewise-hat probability mass law. Averaging W gives mu=(3a²+b²)/(12a), and Haar uniformity of {qX−pY} gives the Bernoulli variance-correction mean 1/6, so nu=(a²+b²+2)/12. Since gcd(a,b)=1, gcd(3a²+b²,a)=1 and denom(12mu)=a. The quadratic for a from S=12nu−2=a²+b² selects the larger nonnegative root; the shape ratio profile 144(1+r²)/(3+r²)^2 goes from 16 to18. Independent exact Fraction integration recovered all five named direction PMFs and moments, including axial and diagonal boundary directions. The a=b endpoint only occurs at a=b=1 by primitivity. No finite test is used for the universal argument.

## originality

PASS

PASS best-of-knowledge. Closest public flat-torus crossing theorem uses TWO independently randomly placed shortest arcs and a random determinant of TWO displacements, with no fixed primitive homology class or marked integer intersection-count law. Glorieux–Yarmola concerns the nullhomotopy probability of random three-vertex minimizing-geodesic triangles. Neither implies the marked count PMF or the exact mean denominator inversion. Classical Crofton/Buffon methods motivate the phase representation but no inspected source yields this arithmetic inverse.

## value

PASS

PASS: the inverse problem of recovering a primitive integral homology class, up to signs and axis exchange, from a scalar marked random-intersection statistic is a natural exact marked-length/intersection invariant. The metric aspect invariance and exact integer denominator extraction are nontrivial: these distinguish a topological homology parameter from geometric shape without a noisy-data claim. The complete rational count law and second moment provide independently useful information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
