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

For each ordered side pair, the arclength expectation uses product length measure divided by (2+t)², followed by division by (2+t); the same-side integrals are a³/3. For unlike sides, homogeneity gives the factor 3 in divergence of (x f,y f) for f(x,y)=sqrt(x²+y²−2qxy); only the two outer edges contribute. Using J(z;k)=(z sqrt(z²+k²)+k² asinh(z/k))/2 on each edge yields the displayed integrals: on equal legs the log ratio is (1−q+t)/(1−q)=(2+t)/t, and on a leg/base pair the two edge logs reduce to H and L respectively. Summing two ordered leg/leg and four ordered leg/base terms proves the formula at all 0<t<2. Differentiation and the identity L−H=−(t−1)K give F=−(t−1)G. At the small end A/t>=8, L>log 16>8/3, H<=256t/255 and the polynomial is >=−14t. At the large end A<0, L>=2/(t+1) by the atanh bound and H>3 by the first five positive series terms; the resulting upper bound on F equals (t−2)(11t+9)/(t+1). Each inequality has the required coefficient sign. On the middle interval the independent rational enclosure covers every subinterval including t=1; positivity proves both strict branches. Expanding exact log and analytic factors at t=0 and s=2−t=0 gives the stated remainders and coefficients. R(1)=(2+log 3)/18, R'(1)=0 and R''(1)=4(1−log 3)/81; analyticity there gives the quadratic deficit. The common endpoint limits 1/6 together with strict monotonicity yield the exact range and equality case.

## originality

PASS

The supported distinct claim is the explicit first-power isosceles shape profile, strict unimodality and unique equilateral maximizer, with the resolved degeneration expansions and local deficit. The strict universal lower bound is known. The same-day fixed-width-profile theorem actually covers the leading flattened-triangle logarithmic coefficient, but not the finite linear coefficient, the short-base degeneration, or the global profile. No priority is asserted for the covered parts or inferred from same-day dates.

## value

PASS

Boundary mean chord length is a canonical geometric statistic, and isosceles triangles provide a natural continuous family with two inequivalent degenerations. Knowing the complete monotonic profile, sharp unique equilateral extremum and exact rates resolves a shape question the convex-class bounds and leading thin-lens asymptotic do not. A researcher comparing collapse mechanisms can use the precise rates and finite coefficients rather than just a common limiting value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
