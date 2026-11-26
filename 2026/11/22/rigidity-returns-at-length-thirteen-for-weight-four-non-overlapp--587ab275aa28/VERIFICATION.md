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

All 715 weight-four words have rotation orbit size 13 by primality and nonconstancy. For a nonzero cyclic shift, one of the two words' proper prefixes is the other's suffix, so a code uses at most one word from each of 55 necklaces. Length-one overlaps require opposite symbols at each word's endpoints and the same starting symbol throughout any nonempty code. Reversal exchanges the two uniform orientations and preserves non-overlap. In the 1-to-0 orientation the thresholds are equivalent to 13 times every proper prefix weight exceeding four times its length. Complementing with a proper prefix gives the strict reverse inequality for suffixes, proving compatibility. In each necklace the minimum of the integer cyclic partial sums with increments 13w_j−4 is unique among the 13 starting positions, since 13 does not divide 4k for 0<k<13. The rotation after the minimum has all proper partial sums positive and is the threshold representative, so the code attains 55. For rigidity, the independent bit-mask reconstruction filters self-overlaps, tests both directions of every proper overlap and partitions the 89 candidates into all 55 orbits. Every size-55 code must choose exactly one from each. The independent exhaustive domain search gives exactly one solution with 1-to-0 endpoints and it equals the threshold code. Independent replay verifies each of the 55 supplied singleton-forcing rows against all remaining compatible representatives; the reverse solution is distinct and there are no other orientations.

## originality

PASS

Pass is for the complete labeled optimizer classification at (n,w)=(13,4), not for obtaining the value 55 by the standard coprime-composition rotation construction. The strongest exact indexed weight-four tables stop at length 12, the all-length optimizer classification found concerns weight three, and the same-day four-marker prefix-normal records study individual cuts of a necklace rather than compatibility across a codebook.

## value

PASS

Length 13 is the first instance after the documented strict loss at length 12 and thus a motivated first test of rigidity at resumed full packing. The nontrivial fact is that even though 31 candidate orbits have multiple initially admissible rotations, every globally compatible maximum selection is forced up to reversal. This determines all maximum labeled codebooks, not merely another tabulated size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
