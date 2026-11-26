---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Count each diagonal output with weight 2 and each off-diagonal output with weight 1. The total weighted incidence is at most 2q²+2q. Each constant word uses weight 2 and each other word uses at least 3, giving 3|C|≤2q²+2q+p≤2q²+3q for p constants. In an unselected Steiner block the four distinct permutations are two reversal pairs; each reversal pair supplies each ordered off-diagonal pair exactly once. For a selected ordered block (a,b,c), the three distinct words abc,bca,cab cover ab,bc,ca twice and ac,ba,cb once; aac,bba,ccb supply exactly the latter three missing off-diagonal incidences and add aa,bb,cc once each. Blocks share no unordered pair, and the selected parallel class covers all letters exactly once, so adding all constants gives two incidences at every output without duplicate words. The classical existence theorem for resolvable Steiner triple systems supplies a design for every q≥3 with q≡3 mod 6. In that congruence class the weighted upper bound is integral without loss by rounding. Sharpness forces every output saturated, all constants present and every nonconstant word to use exactly weight 3. A two-letter word can then only have an adjacent repeat; each doubled letter occurs in exactly one such word because its diagonal has one remaining incidence. This verifies the capacity and stated necessary rigidity.

## originality

FAIL

A distinct indexed theorem covers the exact same bound, the sharp capacity on the entire assigned congruence class, and its attainment by a construction from any Kirkman system. Its incidence inequalities force the remaining rigidity immediately. The alternate local six-word template is a correct variant, not a new mathematical capability. This is verified coverage; the later displayed date of the overlapping record does not determine publication priority or provenance.

## value

FAIL

The short-block capacity is a natural useful quantity in isolation. Against the verified stronger theorem, the residual explicit observation is the unavoidable equality case of the same two resource bounds, and the different concrete block template has the same parameters and guarantees. The record adds no further independent classification or capability beyond that verified mathematical coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
