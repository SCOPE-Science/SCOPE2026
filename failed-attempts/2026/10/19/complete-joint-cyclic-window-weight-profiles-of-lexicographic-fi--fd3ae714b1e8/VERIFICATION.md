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

In least-significant-bit-first integer evaluation order, the least active index s gives blocks of length r=2^s and pairs of complementary blocks. Each cyclic downward transition of the upper-bit truth table joins exactly two zero blocks. Among its cyclic increments, the last (longest) carry occurs twice, while each shorter carry through j+1 bits occurs 2^(k-j-1) times. Prefix parity is an invertible change of variables, so half the toggle count has the asserted polynomial, including the k=0 and k=1 boundaries. The zero-window counts recover runs by second differences. Mixed runs determine s and t, while a pure run of length 2r at the upper endpoint equals the pure-run profile of the next scale. The constant words are separated by W_1, and the two alternating words have the unique nonconstant doubleton profile. As a separate finite check, audit_rm.py built affine words as bitsets, intersected successive circular rotations of the zero-symbol bitset to count starts directly, and verified every coordinate of every joint profile and the parameter multiplicities for 1≤m≤10. The range of the theorem is justified by proof, not by this replay.

## originality

FAIL

The earlier ordered RM(1,m) result is not merely a list of independent marginals. Its proof fixes a parameter pair for each word, gives that word's weight simultaneously for every window length, and counts exactly the words with each pair. Its steps 1–3 already contain the same run law and parameter multiplicities. Its step 4 also identifies adjacent endpoint overlaps at b=2. For nonconstant words, W_2−N/2=H−j, so a value in the interior of one dyadic interval determines (H,j) uniquely. At an overlap, (H,H/2) and (H/2,0) both give H/2 runs of length 2B and hence the identical whole vector. The constants are distinguished by W_1. Thus (W_1,W_2) determines the full vector and the frozen counts and multiplicities follow directly from the earlier result. This is established prior coverage by implication even though the earlier headline is about marginal enumerators.

## value

FAIL

A joint spectrum is a natural object and marginal spectra need not in general determine it. Here the available prior wordwise result is an exception: its b=2 endpoint arithmetic and run law already give the full joint census by direct combination. What remains is an explicit restatement and deduplication, not an independently useful new exact fact under the value standard. No distinct valuable narrower theorem was established for repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
