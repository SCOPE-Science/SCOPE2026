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

The four distinct eigenvalues and Lagrange spectral projectors reproduce all four off-diagonal formulas in RESULT.md; the diagonal weights are nonnegative and include 1/4 from the constant vector. For t>0, 0<C<B<A<1 makes both adjacent classes strictly positive. Direct matrix powers give (L^2)02=1, (L^3)03=-1 and (L^4)03=-6. Thus G and F have respectively simple and double zeros at zero and are negative immediately to its right. With x=exp(-t), the ordered-power Descartes bound gives two and three real t-zeros counting multiplicities. For that bound, divide out the lowest power and induct by differentiating. If the first two signs agree, the derivative starts with the same sign as the function's constant limit at x=0; before the first function zero it must already have a zero by the mean-value theorem. This is the extra derivative zero in the same-sign case. The positive limits at infinity then force precisely one simple positive root each. This proves the inclusive maximum cutoff with t=0 separately and strict positivity beyond it. At t=eta*u the leading scaled polynomials are 2u(u-2) and (2/3)u^2(u-6), uniformly on compact u-sets. At s=eta*t, the squared-L rates have the same Descartes patterns and first nonzero small-s coefficients -4s and -12s^2. At s=1 use g<3/4, exp(-4)<1/16 for G>0, and 6-4sqrt(2)<0.35, g>0.7, exp(-a)>1-a for F<0. The roots converge by bracketing on both sides of simple crossings; this also gives continuity at finite eta, hence attainment of a positive maximum since the horizon goes to zero at both ends. Independent replay: python3 -B /workspace/branches/independent_replay.py 1 (SymPy and mpmath), with exact projector and joint Taylor checks and numerical strong-limit roots 0.2328189247758518 and 1.5526760566350351. The uploaded checker was read, not run; no sampled times were used for exhaustiveness.

## originality

PASS

Pass the distinct result for the full P4 semigroup with finite positive mixing, including the weak-mixing crossing laws. The squared-L endpoint equation and its unique recovery at the order-two endpoint are shared with a distinct same-day record and should not be credited as a separate novel endpoint calculation. No inspected source covers the finite-mixing two-barrier theorem. This is not a priority ruling between same-day records.

## value

PASS

P4 is the smallest path on which both distance-two and distance-three channels can obstruct all-entry positivity. The exact time set and the distinct onset scales answer when a mixed generator whose semigroup is not all-time positive nevertheless becomes positive; the two scales cannot be obtained from a generic eventual-positivity theorem. Finite-mixing root ordering, uniqueness of the worst strength, and extensions to longer or weighted paths are not established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
