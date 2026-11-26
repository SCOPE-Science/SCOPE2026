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

The even Gram reduction gives the stated two numerators and denominator Δ=e^(−2at)(e^(2at)−1−2at−2a²t²)>0. After multiplying the outer integrand by its positive exponential, its second derivative on 0<xt<at is 4(at−xt)e^(2xt)>0, and beyond at its slope is e^(2at)−1−2at>0. For the center the exact exponential numerator has no terms before t⁴; the degree-four bracket is −a²+12a−6. For degrees five and six the brackets increase in a and are already positive at 1/2, below the root. For j≥7 the highest two coefficients are 2^(j−2)(j²+3j)−4j² and 2^(j−2)(8+3j−j²)−4(j+1). They have opposite signs and positive sum since 2^(j−2)≥4j, so together contribute positively for 0<a≤1. Keeping just the degree-two and degree-four terms suffices because a_*²>1/4 while 4/[(j−2)(j−3)]≤1/5. This proves strict positivity at the cutoff even though the leading t⁴ term vanishes there. Below it the leading term is negative, whereas c,d→0 and b₀∼4/t gives eventual central positivity. The endpoint a=1 has b_a∼2/t and causes no exception.

## originality

FAIL

A separate published catalogue entry gives the same full sign theorem and also provides the exact flat limits of all weights. The sole convention change for the theorem is dx/2 instead of dx, which multiplies the weights by the positive factor 1/2 without changing signs or the cutoff. The demonstrated equivalent coverage blocks validation; it does not establish within-day priority, authorship, or dependence.

## value

FAIL

The sharp sign frontier would be useful for designing positive kernel quadrature at arbitrary bandwidth. But the frozen contribution is that exact frontier and its two limiting signs, all already available from a distinct theorem by rescaling. The alternative coefficient argument does not establish a separate scientific claim, wider applicability, or a new crossing result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
