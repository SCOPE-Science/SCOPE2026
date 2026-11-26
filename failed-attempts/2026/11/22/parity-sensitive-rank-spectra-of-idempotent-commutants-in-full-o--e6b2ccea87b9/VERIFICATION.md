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

An injective idempotent is a partial identity on its domain. Commutation with 1_B is exactly equality of the membership bits at x and f(x) for every domain point. A positive translation has r distinct strict edges in a forest, so each of its binomially many domains has 2^(n−r) commuting idempotents. An order-decreasing restriction of a reflection may choose only the larger point of each exchanged pair and the center, if any; consequently its rank-generating local factors are 4+2z per pair and 2(1+z) at the center. Put ℓ=min(s−1,2n+1−s); floor(ℓ/2) is the pair count, with a center iff ℓ is odd, and each ℓ below n occurs twice while n occurs once. The binomial sum then gives both reflection corrections, with the even top and odd top coefficients as stated. Empty and singleton maps are counted once by using the reflection sum only at r≥2. An independent actual-map enumeration and explicit composition with every partial identity reproduced every coefficient for n=1,…,8.

## originality

FAIL

Material coverage is in the proof of the distinct same-day Resultary record 2523a33ab907, not in its ungraded headline total. It gives the exact admissible-domain reflection intervals by length (two of each ℓ<n and one of ℓ=n), the center rule, and the four separate weighted choices per swapped pair. Discard choices containing the smaller point of a pair (its image would be larger) and mark the one remaining selected-point choice with z. This mechanically gives 4+2z from the listed weights 4,2,2,2, and marking the center gives 2(1+z). Keep the negative-displacement translation and mark by rank in the prior binomial sum. These operations already give the whole restricted polynomial, with the prior rank-zero/rank-one overlap dealt with by retaining only rank≥2 from the reflection part. Its displayed binomial closed forms and top ranks are direct coefficient extraction and a hockey-stick sum. The comparison is about derivable coverage, not a claim that the exact closed forms were printed earlier or an inference of priority from the shared date.

## value

FAIL

Rank is a natural statistic, and the formulas are correct and convenient. Here all of the proposed gains, including the parity-dependent top ranks, follow by retaining one already enumerated orbit choice, marking it, and extracting binomial coefficients from the inspected factorization. The record does not establish a distinct structural obstacle or a precise unknown invariant beyond this mechanical specialization. No surviving independent claim warrants repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
