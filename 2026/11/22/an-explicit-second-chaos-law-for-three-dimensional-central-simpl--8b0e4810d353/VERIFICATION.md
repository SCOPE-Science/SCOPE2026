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

For fixed noncollinear directions x,y, the other pair has opposite normal signs with probability 1/2. Conditional on this, the intersection direction of their segment with span(x,y) is uniform by rotations about the normal. A strictly positive convex dependence exists exactly when the negative intersection direction is in the open cone between x and y, yielding theta/(4 pi). Boundaries are null. The angle density sin(theta)/2 gives mean pi/2, hence depth mean 1/8, zero first projection, and the stated centered second kernel. An independent spectrum check uses the operator H with kernel sign(x·y): its squared kernel is 1-2theta/pi by the area of two spherical lunes, so T=-H²/8. Funk–Hecke gives H zero on even modes and eigenvalue integral_0^1 P_(2m+1)(t) dt=(-1)^m(a_m+a_(m+1))/(4m+3)=(-1)^m a_m/(2m+2) on the odd modes. Squaring gives exactly the stated lambda with multiplicity 4m+3. Canonical Hoeffding components have variance ||h_j||²/binom(n,j); at n-scale only the second term with multiplier 6 remains. On finite harmonic sums the multivariate CLT and the law of large numbers give independent centered chi-squares; the exact canonical variance bounds the omitted Hilbert–Schmidt tail uniformly. Integration of theta against sin(theta)/2 gives variance (pi²-8)/4, so the n² variance limit is 72||h2||² = 9(pi²-8)/(8pi²). The sum of multiplicity times |lambda| telescopes to 1/8, so the nonnegative chi-square series has finite expectation and converges a.s. by monotone convergence (not merely by L1 convergence alone); centered partial sums converge in L² by the squared-eigenvalue sum. Independently small finite prefixes and a sufficiently small independent tail with positive probability give the upper endpoint 3/4; the first chi-square is unbounded, so the lower endpoint is -∞. Positive radial rescaling preserves the sample event by renormalizing its nonnegative dependence coefficients.

## originality

PASS

The mean and generic central degenerate-depth asymptotic law are prior theory. The supported distinct content is the explicit tetrahedral projection and its evaluation to a complete spherical spectrum, variance and support endpoint for this law. The strongest accessible depth comparison gives only the operator-eigenvalue template, and nearby indexed explicit laws concern triangles in the plane. Priority against the inaccessible 1992 full text remains a bounded risk, not a negative inference from unavailability.

## value

PASS

The canonical central three-dimensional sampling model is independently motivated. A fully explicit non-Gaussian law with exact normalizing variance and finite upper endpoint offers interpretability and a reference distribution beyond abstract degeneracy or an unspecified operator. The generic n-scaling and mean are not credited as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
