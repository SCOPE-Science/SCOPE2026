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

Greedy complete-alphabet arch factorization proves every k-universal word has ≥qk symbols. For q>=3, (01...q−1)^(k−1)(0 2...q−1 1) is qk long and unbordered because any suffix beginning in 0 starts at a block boundary while nonempty block-aligned prefixes finish q−1 rather than 1. For binary length 2k, every arch is an opposite-bit pair; comparing first/last arches forces a border of length 1 or 2 when k>=2. A normalized extra-symbol first arch starts 001 and remaining arches pair, and explicit even/odd border comparison yields C_k constraints. Complements and reversals yield four disjoint families. Independent direct enumeration through k=7 recovered minimum lengths and counts k1..7: (2,2),(5,4),(7,4),(9,8),(11,12),(13,24),(15,44), with no shorter unbordered k-universal words. Infinite proof supplied by arch/border arguments.

## originality

PASS

Combines two natural, separately developed word constraints; exact q-dependent length obstruction and complete binary shortest boundary are not implied by generic arch ranking or generic border ranking, or by the narrower Lyndon optimum theorem.

## value

PASS

Minimum word length under simultaneous subsequence coverage and border avoidance is a canonical intersection of two well-motivated combinatorics-on-words constraints. Its alphabet-dependent threshold and entire boundary classification are useful exact finite-language invariants, not a tiny instance or a routine renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
