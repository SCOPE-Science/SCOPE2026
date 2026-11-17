---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

For any ordered induced seven-tuple w_i in C_n^p, cyclic positive gaps g_i sum to n. Each nonedge w_i-w_{i+3} forces 3-gap sums ≥p+1 and their complements >p; summing yields 3n≥7(p+1). Since a two-gap arc is smaller than a forbidden three-gap arc, adjacency of the index-distance-two pair forces each two-gap sum ≤p; summing gives 2n≤7p. Conversely w_j=⌊jn/7⌋ yields 1- and 2-step clockwise distances ≤⌈2n/7⌉≤p and 3-/4-step distances ≥⌊3n/7⌋≥p+1 in both directions, proving the iff interval for cyclic-order-preserving induced C7². The ordinary 3-cut complex of C7² has seven tetrahedral facets and collapses via 25 free-face pairs to S¹ (seed homotopy already Bayer et al Proposition 7.27). The link of the complement of this induced subset in the ambient ordinary 3-cut complex equals the seed cut complex. A pure shellable complex would have shellable links, whereas the pure 3-dimensional seed has nonzero H1; hence nonshellability. Independently exhausted seven-subsets for p=2..4; this only checks bounded cases, while the gap proof handles all p≥2.

## originality

PASS

The seed S¹ and nonshellability are explicitly prior results; the new statement is the sharp all-p cyclic-order embedding interval and resulting infinite subband of an open nonshellability region. Earlier powers-of-cycles paper proves shellability n≥6p−3; this band lies below and does not follow from that direction. A different 8-vertex motif interval and stable-range cyclic representation results do not imply the sharp 7-vertex motif interval. PASS is for this final combined claim, not for the known seed calculation.

## value

PASS

A uniform sharp obstruction criterion inside a published nonshellability conjecture is mathematically motivated: it gives an explicit finite induced motif producing non-shellability for every p, with a tight arithmetic recognition interval. It does not claim full conjecture resolution or optimality among all motifs, and the novelty is not the elementary link lemma alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
