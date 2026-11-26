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

For a proper selected subset, each new transposition merges two permutation cycles, so the final permutation's cycle supports equal the forest components. Only distinct spanning paths can therefore collide among proper subsets. The full cycle word splits the spanning-tree permutation into two cycles at its last switch, so it can collide only with a word missing two edges. Both types of comparison cancel to t_j U = U t_i, with U the intervening product. Each component of the cycle minus those two edges contains one endpoint of each deleted edge; transport within each component must cross every path edge, hence the omitted edges must be the first and last. With every path edge used once, each starting endpoint reaches its opposite endpoint exactly when the traversals are in increasing chronological order on both arcs. This covers the zero-edge path case when the extremes touch and k=3. It yields precisely two distinct size-two fibres (the two output cycle counts differ). Interleaving the two increasing arcs gives k*2^(k-2) schedules. Doubling two masses gives Shannon loss 4/2^k, max mass 2/2^k, and collision sum (2^k+4)/2^(2k); the order average loses exactly 1/(k-1)! bits. Forest injectivity also follows from the component partition. Scope is distinct transpositions used once and fair independent bits; only the last average needs a uniform public order. The all-k proof is decisive. The frozen checker was inspected, not run: its displayed counter totals 277398 exhaustive groups +125 sampled orders +246 forest orders =277769; the forest masks are inputs to one check per order, not separate counted groups.

## originality

PASS

The supported distinct claim is the complete fixed-order private-subword fibre classification and resulting conditional entropy law on a simple cycle. The tree-cycle lemma is classical, and the rank-order count and entropy algebra are not asserted as independently new. No inspected distinct result covers the classification or implies it without the additional path-transport argument.

## value

PASS

The single cycle is the first connected departure from universally injective one-pass forests. The classification determines exactly which public schedules lose information and which hidden words are ambiguous, rather than giving only an upper bound, an asymptotic mixing estimate, or computed small cases. This is a useful finite boundary result for distinct-switch networks and is not a cryptographic security claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
