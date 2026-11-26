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

For odd p, the p^j summand in the valuation of a(n,k) counts multiples in [n-k+1,n+k] minus floor(k/p^j). It is nonnegative. For k>=2, every p^j hitting the four central integers contributes at least one: for p^j>k this is direct, and for p^j<=k use floor(2k/p^j)-floor(k/p^j)>=1. Only 3 can hit two of the four integers at the same power, precisely at power 3 and n=1 mod 3. Degree two attains every predicted odd-prime minimum except this case. Then degree four exists, its four added factors are all units mod 3, and its factorial denominator removes one factor of 3. For k equal to the largest power of two <=n, k is even, and 2k+(n-k) has no binary carries, so binom(n+k,2k)(2k-1)!! is odd. This settles the gcd for all n>=2, including n=2,3 with only one retained coefficient.

## originality

PASS

The distinct supported claim is the exact gcd of the positive even-degree coefficients, not the coefficient formula or general positive-row divisibility. No distinct source was found that states this gcd or establishes a stronger result settling it without the additional minimization over even degrees. This is a bounded comparison, not a priority certificate.

## value

PASS

The even projection is the natural parity component (after removing the unit constant); its primitive integer normalization and prime reductions require its exact content, not just an obvious divisor of the Bessel row. The all-index classification identifies a single exceptional odd-prime loss and supplies an even-degree odd witness in every order. This is a modest but complete arithmetic invariant of a standard family, not a proposed new general theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
