---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

For g nonempty disjoint guilds with S species, uniform sampling exactly k survivors gives H_a(k)=[z^k]prod_i((1+z)^a_i-1)/binom(S,k). The coefficient interpretation and inclusion-exclusion are algebraically identical; signs are exact integer differences. Independent partition recursion and polynomial convolution enumerated all profiles with S=1..13 and all 1,355 same-S/g unordered pairs: none reverse at S<=12 and precisely three at S=13, namely (1,3,4,5)/(2,2,2,7), (1,4,4,4)/(2,2,2,7), (1,3,3,3,3)/(2,2,2,2,5). The infinite (1,3,4,m) versus (2,2,2,m+2) m>=5 family has coverage-numerator difference 4(m-4)>0 at k=4 and -1 at k=S-1, proving reversal for every m. Finite exhaustive domain is S<=13 only; higher S covered by an explicit family, not a full census.

## originality

PASS

The 2001 Fonseca-Ganade full paper treats random functional-group loss and expected surviving functional richness, first-loss risk and variance, but does not state this sharp S=13 same-S/g reversal classification. Related Resultary variance and rarefaction reversal findings concern other objective functions or sampling. The first-layer census appears a nontrivial new exact statement, qualified against classical coupon-collector and hypergeometric literature.

## value

PASS

Probability that *every* ecological function survives a fixed-size extinction event is a natural finite-community robustness statistic. A sharp minimum population at which competing allocations can reverse ranking across budgets and the complete first-layer list clarify a mathematically real failure of universal ranking, with both a bounded cutoff and an unbounded witness family. The disjoint-guild null model is explicit and meaningful even without biological empirical validation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
