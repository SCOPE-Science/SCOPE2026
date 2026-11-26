---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For probability measure on the real sphere, every real f is a+Q with Q=xᵀAx trace-free. Gaussian cumulants and polar normalization give EQ²=2p₂/[n(n+2)], EQ³=8p₃/[n(n+2)(n+4)], and EQ⁴=(12p₂²+48p₄)/[n(n+2)(n+4)(n+6)]. At fixed zero sum and p₂, cubic stationarity allows at most two values, whose multiplicities k,n−k give the largest absolute cubic only at a one-outlier spectrum when n≥3. Quartic stationarity allows at most three values; if there are three, the constrained second derivative on a split of a repeated extreme eigenvalue is positive, so both extremes are simple. The zero sum of the cubic roots and the trace condition then force the middle value to be zero for n≥4, giving p₄/p₂²=1/2, below the two-valued one-outlier maximum. For n=2,3 this ratio is identically 1/2. The resulting moment bounds are attained together by the normalized Y_ω. For r=|a|/||Q||₂, their scalar envelope has the stated derivative and the unique positive maximum by the signs and Descartes’ rule; n=2 gives r=√3/2 and quotient 15/7, while n=4 gives γ=1, δ=3, r=1/2 and quotient 21/5. Both excluded pure-component edges have strictly smaller quotient. Cubic equality with a chosen positive constant selects the positive zonal sign for n≥3; for n=2, either sign of a real quadratic is a rotation of the same zonal form. For a complex function the real/imaginary Cauchy–Schwarz bound has equality only when their squares are proportional (or one part vanishes). Real analyticity on the connected sphere then forces the parts to be proportional. These checks establish the global complex result, rather than relying on the supplied 144-assertion report. The frozen checker was inspected, not executed.

## originality

FAIL

The exact mixed quotient was not found verbatim, but the decisive joint moment extremum is a direct specialization of Sharma–Bhandari’s finite-population skewness–kurtosis theorem (which also records the classical sharp marginal bounds). Applied to the eigenvalues, that theorem gives both coefficients, their simultaneous equality law, and hence the full sharp mixed scalar envelope by the usual spherical moment conversion. The claimed ratio and rigidity then follow by differentiation and the standard complexification equality step. The failure is demonstrated mathematical implication, not a keyword miss or inaccessible source.

## value

FAIL

The full quadratic sphere space is natural and the explicit optimizer is useful as an example. However, the sharp fixed-ratio moments and their simultaneous geometry follow by applying the existing joint sample-moment result to the centered spectrum; the remaining calculation is a standard moment conversion, scalar derivative and complex equality reduction. The frozen record establishes no distinct new extremal phenomenon, range or reusable bound beyond this mechanical consequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
