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

Greedy arches show a shortest linear k-universal word has k consecutive alphabet permutation blocks and length qk. Circular marked words are a union of q cut-phase sets. In an intersection of t phases with cyclic offsets g_i, the segment symbol sets in all k blocks are identical, giving q! (Π g_i!)^(k-1) words per selected subset. Each t-subset counted t times by its rooted q-gap composition and q starting residues, giving coefficient q/t. Equal symbol counts imply any period is q e with e|k. Burnside fixed words under rotations are repeated shorter circular universal words, yielding the totient and Möbius divisor sums. Direct independent enumeration generated all word rotations for (q,k)=(2,2),(2,3),(3,2), finding marked/necklace pairs (6,2),(14,3),(78,14).

## originality

PASS

Published work defines circular scattered-factor universality and study repeated words, while Adamson gives linear counts, but the inspected central primary sources do not enumerate overlaps between q phase cuts and primitive rotation orbits for all q,k. General Burnside enumeration only supplies the quotient method after this specific phase-intersection count. Resultary comparisons identified an exact deletion-resilience permutation block result with different quantifiers and distinct circular-avoidance necklace counts, not a dominating theorem.

## value

PASS

Complete all-alphabet shortest-length cyclic-subsequence-universal necklace and primitive-period census naturally sharpens structural universality theory, distinguishing cut overlap and imprimitive repetition from linear permutation-block counting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
