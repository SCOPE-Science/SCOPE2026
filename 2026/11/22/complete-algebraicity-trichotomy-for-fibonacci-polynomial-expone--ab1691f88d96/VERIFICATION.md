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

For arbitrary Z[T], expand Binet's formula into parameters (−1)^i α^(k−2i). At x=α^(−r) for the largest nonzero odd degree r, only the k=r,i=0 term can contribute: smaller odd degrees cannot reach exponent r, even terms have the wrong exponent parity, and sign cannot create an equality since α>1. The residue of E'/E is −a_r/(√5)^r and is irrational. An algebraic series with rational logarithmic derivative has rational residues (equivalently, the norm from a finite extension has logarithmic derivative equal to the extension degree times E'/E). Even weights pair the conjugate parameters into distinct Lucas quadratics and central ±1 factors. Thus 5^h kills all exponent denominators. At the largest j realizing h>0, the exponent of the positive-sign Lucas quadratic has leading term c_j/5^j, and all higher terms have strictly greater 5-adic valuation, even after binomial factors are inserted. That factor is irreducible by its discriminant 5F_(2j)^2. Its order in R=E^(5^h) is coprime to five and forces degree divisible by 5^h (also by taking norms of E^(5^h)=R), and any rationalizing power divisible by 5^h. The polynomial equation supplies the matching upper bound. The h=0 case includes constants and zero, with rational E. The cited integrality criterion applies to T^(2d)−T^(2d−4) for d≥3 and its leading deficit is d. Independently recovered even-weight exponent denominator data by Laurent multiplication and checked 24 exact logarithmic coefficients of the displayed degree-125 powered identity; the general proof is not based on truncation.

## originality

PASS

The integrality criterion, integrality of the mixed example, and the exact monomial degrees for 5T^(2k) are explicitly prior. General Gauss-congruence results also imply algebraicity in the integral rational-logarithmic-derivative subfamily. The supported distinct claim is the full classification including nonintegral and non-even weights, and the uniform exact denominator/degree formula for arbitrary mixed even coefficients. No inspected stronger statement provides that coefficient-level result without controlling inter-monomial cancellation.

## value

PASS

The natural family already arises in an independent integrality study. The parity boundary and exact field degree answer algebraic questions not resolved by that criterion; the valuation maximum computes the precise denominator even when spectral factors overlap. The result resolves the published integral mixed example at degree 125 and gives unbounded degrees with primitive leading coefficient. This is a uniform classification, not a monomial substitution or a finite series calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
