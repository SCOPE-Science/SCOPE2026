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

Reconstructed t=2s2(n)-s2(3n) as carry count in n+2n and proved no isolated carry (first carry forces a second). Carry bound t≤r; if t>0, output popcount b≤r because an output with >r ones would have to be 2^(r+1)-1, which is divisible by 3 only in the alternating carry-free case. Nonadjacent one digits give t=0 length≥2a-1, attained by (10)^(a-1)1. For t≥2 and b,t same parity, explicit (10)^h 1^b or 1^t(01)^h achieve shortest length max(b,t) and required weights. Sum parity-square counts gives C(r,2)+2, r=1 and n=0 included. Independent brute-force enumeration r=1..12 plus witness checks agreed; all-r follows from the carry/witness proof.

## originality

PASS

PASS best-of-knowledge. The primary 2020 Clokie–Lidbetter–Molina Lovett–Shallit–Witzman paper studies the sign event s2(3n)<s2(n) via automata and asymptotic counts; Kaneko–Stoll main theorems bound products with prescribed small weights, not the all-dyadic two-coordinate support or exact minimal witnesses. Morgenbesser–Shallit–Stoll studies parity of digit sums on multiples. A marginal OEIS series and finite small-weight restrictions do not imply the joint all-r classification.

## value

PASS

PASS. The multiplier 3 is the first nontrivial odd binary dilation, and (s2(n),s2(3n)) is a natural statistic in carry propagation, 3-flimsy numbers and central binomial 2-adic valuations. A complete exact support and shortest witness for EVERY dyadic length, with a forbidden single-carry stratum and quadratic count, supply meaningful data not recoverable from marginals or aggregate sign counts. No paper-sized downstream theorem required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
