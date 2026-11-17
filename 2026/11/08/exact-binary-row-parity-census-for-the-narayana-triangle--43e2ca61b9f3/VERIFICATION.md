---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For n even, Lucas submask restrictions and Narayana symmetry yield 2^{s2(n)} odd entries. For n odd, adjacent binary submask pairs sit in blocks of 2^t consecutive indices (t=ν2(n+1)), yielding 2^{s2(n)-t}(2^t−1). Counting free higher bits gives exact multiset over every dyadic range; the even-row and odd-row contributions sum to (5·3^(L−1)−3)/2. Independent exact integer computations checked all rows 1..256 and complete dyadic spectra L1..9. This is an infinite combinatorial proof, not finite extrapolation.

## originality

PASS

An earlier October 18 Narayana valuation-layer theorem explicitly proves the SAME DYADIC TOTAL, and its proof reveals even-row parity counts and odd-row binary submask structure. Those statements and the classical Lucas test are PRIOR and not credited as original. The surviving distinguishable contribution is a complete explicit multiset of the rowwise odd counts A(n) over every dyadic interval, with separate binomial multiplicities; the published aggregate A0(L) does not determine this full histogram by itself. That extension is a short binary-block argument and its limited incremental priority/value must be represented precisely.

## value

PASS

A natural OEIS Narayana-row statistic has a closed all-index binary description and, additionally, a complete value distribution at every dyadic scale rather than only its aggregate first moment. The distribution can compute other counts and functions of row parity directly. Value is the exact natural invariant/histogram, not re-proving Lucas or previously published dyadic total.

The dated certificate retains the supplied scientific assessment, sources and limitations.
