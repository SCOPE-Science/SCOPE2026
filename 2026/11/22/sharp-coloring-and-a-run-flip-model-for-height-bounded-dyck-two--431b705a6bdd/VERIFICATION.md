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

In the strict ceiling two, odd prefix heights must be one; even heights can be zero or two. This corrects frozen line 37, which says the intervening heights are always one or two. The internal pairs are exactly 10 or 01. An edge in the Dyck graph differs on full pair blocks and is Type A exactly when a consecutive block of equal orientations flips. XOR by the alternating mask turns these into alternating-interval flips; intervals of length at least two give the unrestricted two-read deletion graph and singleton flips give the cube, disjointly. One can check the Type-A criterion directly in the equal-content case: if deletions are at different positions, their alignment is a left or right shift on the first-to-last mismatch interval, and each orientation determines at most one descendant by shifting the deletion within equal runs to those two endpoints. Both orientations are possible exactly when the mismatches alternate; they then give distinct descendants. Counting intervals gives the degrees and edges including the empty bit vector. Trimming fixed endpoints preserves all Type-A adjacencies and sends the clique to the standard fixed-weight clique; the component coloring comes from the number of 01 pairs. Independent deletion-bucket enumeration through semilength eight checked the checksum, clique, constant-run graph, direct shortened deletion decks plus cube, degree maximum, edge totals and induced five-cycle. The all-parameter isomorphism is proved, not extrapolated.

## originality

PASS

For the narrowed result only: the height-two identification with the edge-disjoint union of an unrestricted binary deletion graph and a cube is a structural correspondence, not a claim to rederive known checksum, clique, odd-hole, edge or degree results as independently new findings. The inspected circle of related exact records does not state this identification or mechanically provide the Dyck pairing and mask that realize it.

## value

PASS

The remainder gives a complete edge-preserving reduction for the natural two-level Dyck channel. It replaces deletion-deck comparisons of length 2n by an unrestricted graph with n−1 coordinates and exactly one additional edge type; this determines every neighborhood and permits transfer of structural information, not just two known totals. Known color and degree identities illustrate the transfer rather than carrying the value assessment by themselves.

The dated certificate retains the supplied scientific assessment, sources and limitations.
