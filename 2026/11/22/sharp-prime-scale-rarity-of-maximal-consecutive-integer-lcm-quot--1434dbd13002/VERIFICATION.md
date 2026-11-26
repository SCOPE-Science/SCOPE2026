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

Fix k before taking the density in n. For p^j<=k the local quotient valuation counts the multiples in the window minus one, and for p^j>k the contribution is zero. Subtracting from the Legendre sum for k! leaves nonnegative deficits: none when p^j divides m=k+1, and otherwise one minus the carry from adding m to n-1. Local equality forces all carries at and after the first nonzero digit of m in the retained positions; the respective digit counts are free, a_t, then a_i+1. Thus positive local densities multiply by the Chinese remainder theorem, and k! is attained. With J=floor((log m)^3), the primes up to m/J contribute O((m/J) log m)=o(m/log m); all others have exponent one and give log fractional parts of m/p, with prime divisors of m treated separately. On m/(j+1)<p<m/j, dyadic shells of size u in the fractional part have lengths O(um/j^2) and logarithmic loss growing only linearly in shell index. Brun–Titchmarsh at length at least m^(2/3) bounds total truncation loss by O(eta m/log m); shorter shells are nested toward the endpoint in a union of length O(m^(2/3)) per j and cost O(J m^(2/3) log m). Here eta=(log m)^(-2). For bounded truncated log values at the jumps, the variation is O(J log(1/eta)); partial summation with the stated PNT error replaces the prime sum by m/log m times its integral up to o(m/log m). The integral tail and clipping costs are O(1/J) and O(eta) by summing (j+u)^(-2). Integration by parts of log(u)/(j+u)^2 gives -log(1+1/j)/j, with the zero boundary term made finite using 1/j-1/(j+u). Replacing m by k does not change the limit.

## originality

PASS

Pass for the explicit sharp growing-window asymptotic, not the already covered finite frequencies or least periods. The same-observable Gaussian result is particularly close but does not estimate the rare endpoint atom; neither related statistic or the checked exact finite law supplies the derived rate without further asymptotic analysis.

## value

PASS

This determines how often a classical sharp extremum of a natural consecutive arithmetic function is actually realized. It identifies a prime-scale exponent and a definite constant beyond the finite distribution, addressing a far-tail event not accessible by a typical-window CLT. The analytic control of prime intervals near singularities is substantive for obtaining that sharp rate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
