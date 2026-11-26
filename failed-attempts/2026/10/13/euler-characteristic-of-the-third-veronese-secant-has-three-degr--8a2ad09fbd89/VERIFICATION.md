---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The frozen totals are (n+1)², (n+1)²+binom(n+1,2), and (n+1)(2n+1). For B>d, a diagonal cocharacter of weights B^i separates the degree-d monomials by base-B uniqueness and preserves both secants. For a monomial the catalecticant rank equals the number of divisors of the specified degree: differentiating by distinct divisor monomials gives distinct nonzero complementary monomials. For two variables x^a y^b, a≥b, the degree-b divisor count is b+1. The first and second finite differences in the proof realize border rank at most two for b=1 and at most three for b=2, attaining the lower bounds. Support of size ≥4 fails by the first catalecticant; support of size three in degree ≥4 fails by the four quadratic divisors x², xy, xz, yz with x a repeated variable. In degree three the only remaining type is xyz. In Han's normalized ternary cubic its coefficient φ_012 is the sole nonzero coordinate; equation (2.3.1) evaluates to φ_012^4≠0. Projection onto the three support variables sends sums of ≤3 powers to sums of ≤3 powers or zero, so the exclusion holds in larger dimension as well. Thus the pure powers and the ordered b=1 types give m² points for m=n+1; the b=2 types give none for d=3, binom(m,2) for d=4, or m(m−1) for d≥5. Localization and subtracting the closed second secant give the frozen totals and exact-layer values, without implying that the cubic exact layer is empty. The symbolic checks do not rely on rerunning the described finite checker.

## originality

PASS

The inspected sources do not state the third-secant Euler trichotomy or a larger Euler theorem of which it is directly a specialization. The indexed rank-two and osculating Euler results apply to different loci. The assessment credits only the distinct Euler aggregation, not the monomial border-rank tests, which are already available from primary results. This limited distinction does not suffice for the value axis.

## value

FAIL

The invariant is natural, but the remaining numerical increment is mechanically obtainable from results already available for this computation. Theorem 11.3 of Landsberg–Teitler gives every binary border rank b+1; the known divisor-count flattening test discards larger supports with immediate degree-one or degree-two counts; setting all but one coefficient to zero in Han's displayed equation settles the sole surviving larger-support pattern. Under the same monomial localization already used for the lower secant, this leaves only counting ordered versus unordered pairs, and the exact-layer invariant is subtraction of the known baseline. The frozen trichotomy is correct and separately phrased, but no additional gap in the underlying rank geometry or Euler computation remains beyond this routine aggregation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
