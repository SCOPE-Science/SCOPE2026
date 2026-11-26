---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The statement holds for finite simple trees with one uncovered vertex, including the singleton. Two perfect matchings in a forest cannot differ because their symmetric difference would contain an alternating cycle, so there is exactly one near-perfect matching for each exposed vertex. For different exposed vertices u,v, the symmetric difference is the unique u–v path, an even alternating path. Exchanging successive pairs attains half of its length; each flip moves the exposed vertex by exactly two tree edges, giving the lower bound. The partial exchanges put every even-indexed path vertex in D and every odd-indexed one in A, so D is independent and the induced core is connected. Each a in A has at least two D-neighbors: expose one of them and flip toward a to expose its matched neighbor. Matching saturation gives |A|≥|D|−1, whereas the edge count of the core gives |A|≤|D|−1. At equality each a has exactly two core neighbors and is always matched into D; all fringe matchings are therefore forced internally. A fringe component attaches by exactly one edge because the host is a tree and the core is connected; no such edge meets D by the definition of A. The admissible flips are exactly the distance-two exposed pairs, so suppressing A yields the flip graph. Conversely, rooting any tree at the prescribed exposed vertex and matching each subdivision vertex to its farther endpoint gives the intended configurations, with any matched fringe forced by saturation. This proves the classification and the metric, including zero distance. I independently enumerated connected acyclic edge sets through odd order seven and all near-perfect edge subsets in them, checking the core, forced components, adjacency and all distances, plus a 13-vertex example with two matched fringe components at the same subdivision vertex. There were 1,3,120,14700 matched hosts at orders 1,3,5,7. Replay: python3 -B /workspace/reproductions/check.py 1; output /workspace/reproductions/1.log. The supplied checker was inspected, not run; the finite tests corroborate the arbitrary-tree proof.

## originality

FAIL

The complete statement is a direct tree, deficiency-one consequence of existing matching structure and alternating-path/no-detour results, not just the already credited metric or extremal count. Gallai–Edmonds supplies the exposed set, saturated neighbors, perfect fringe, and the surplus-one Hall condition. Its odd components must be singletons in a forest, and the core is connected by the published alternating-path argument. The tree edge count then forces each neighbor to have degree two in the core, making suppression the canonical flip graph. The converse is the elementary rooted construction on once-subdivisions with forced fringe. The classification need not have appeared verbatim for these implications to cover it.

## value

FAIL

The host and classification are natural and the presentation is useful exposition. As an independent finding, however, the decorated core is forced by a standard maximum-matching partition with deficiency one, connectedness and one edge count. The isomorphism, metric and realization then follow by the known exchange rule and rooting. No independently substantive strengthening or new invariant beyond that direct deduction is supplied.

The dated certificate retains the supplied scientific assessment, sources and limitations.
