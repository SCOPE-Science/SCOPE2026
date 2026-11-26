---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For first value k, every smaller value must precede every larger value to avoid 231 and the smaller values must be increasing to avoid 321. This proves the direct-sum decomposition with blocks (a,1,...,a-1); cross-block triples cannot realize the two forbidden patterns because later blocks have larger values. If one swaps the first two positions of a nonsingleton block, the result is the split [1,a-1]; a swap later in a block creates a descent under the block maximum, hence 321. At a block boundary, a left singleton gives the inverse merge, and otherwise the maxima of the two blocks plus the left block's moved last value exhibit 231. Thus precisely those cut bits immediately after a previous cut (with the artificial cut x_0=1) can change. The degree is 1+the number of ones before the last bit, giving the stated multiplicities, edge count and leaf words, including n=2. From any x to y, set the first m-1 bits to one from left to right, set the last bit to target, then restore predecessors in reverse order. This costs at most 2m-1. Between the two leaves, to flip the final bit every predecessor must have been one, so each of these initially and finally zero bits costs two flips. The reflected list has a legal bridge because its prior-level end word has a final one, and the leaves forbid a Hamilton cycle when n>=3. Independent finite replay through n=8 rejected a permutation if any third entry in a triple was below both earlier entries. Generated all legal adjacent permutations directly and extracted prefix cuts by max(p[:i])=i, comparing every adjacency. BFS in these permutation graphs gave vertex counts (2,4,8,16,32,64,128), edge counts (1,3,8,20,48,112,256), diameters (1,3,5,7,9,11,13), and the expected binomial degree rows. Also checked the reflected words as i XOR (i>>1), least significant bit first, for m=1,...,13. The frozen verifier was inspected as text; the all-n justification is the direct proof, not these checks.

## originality

PASS

Best-of-knowledge pass for identifying all legal adjacencies of the permutation graph with one-sided facilitation and computing its full local degree law and sharp all-pairs diameter. The permutations' composition decomposition, the East configuration rule itself, and existence of an adjacent-position Hamilton path are prior. In particular, the frozen prior-work note is incomplete: reverse-complement, unlike inversion, preserves position adjacency and transports Barcucci–Bernini–Pinzani's Hamilton path to this graph. That corollary is not credited as original here; it is not the basis of the frozen originality assessment, which rests on the full mobility geometry.

## value

PASS

The mobility law concerns the full natural induced graph on a classical doubly restricted class. It gives direct legal-move recognition, the exact distribution of available moves, and a worst-case optimal route length, with the two least-mobile states furnishing a tight pair. A prior adjacent-position enumeration by Hamilton path cannot answer these shortest-path or local-mobility questions. This is an exact structural reconfiguration result, not a stochastic East mixing claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
