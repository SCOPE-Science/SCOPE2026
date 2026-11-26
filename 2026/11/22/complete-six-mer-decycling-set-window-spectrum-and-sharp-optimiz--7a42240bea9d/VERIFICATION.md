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

The 14 right/left rotation orbits are vertex-disjoint directed cycles, including the two loops. Any minimum set must delete at least one vertex per orbit. Independently tested the given 14-vertex witness, so the minimum cardinality is exactly 14. I enumerated all 181,398,528 labeled one-per-orbit transversals with no partial-graph pruning. In each full survivor set A I iterated A <- A intersect N+(A), with N+ the outgoing-neighbor union. A vertex surviving t rounds is the endpoint of a residual walk of t edges; a nonempty fixed point means a directed cycle, and on a DAG the round giving the empty set is the longest path in vertices. The exact count and all 14 histogram bins agreed. Complement is a digraph automorphism and reversal an orientation-reversing isomorphism; both preserve the vertex length. On the 408 minimizers, exhaustive independent action evaluation gives fixed counts 408,0,0,4 for identity/complement/reversal/reverse-complement. Burnside gives 103 orbits, two of size two (both canonical masks match) and 101 of size four. The 48-at-26 endpoint and optimizer percentage also agree.

## originality

PASS

The supported contribution is the complete frequency distribution and optimizer count/orbit classification for the labeled binary order-six digraph, not its already-published minimum-set total, extremal path lengths, or generic enumeration methods. The frozen record already makes this distinction expressly in its proof and prior-work section.

## value

PASS

The graph and optimization measure are motivated by the earlier study of exact residual-path guarantees over all minimum decycling sets. The known total and extrema hide how rare either endpoint is. The exact frequency and stabilizer census resolve that gap at a size with tens of thousands of admissible sets, giving reference data for exact graph algorithms and optimizer enumeration; the symmetry result also states which involution accounts for the exceptional smaller orbits. This is not a recomputation offered as new of the known endpoints.

The dated certificate retains the supplied scientific assessment, sources and limitations.
