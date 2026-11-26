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

A new pair has both endpoints in the original target set T, so rows outside T never change; the consequences of every such constant row were already inserted in round 1. Vertices of T gain loops at round 1. Every earlier edge on T is reversed by round 2 using the source's loop, while newly added consequences are symmetric. Thus the update on T from round 2 is Boolean squaring of a reflexive symmetric relation, giving distance at most 2^s after s more rounds. The only way to have diameter n−1 would be a spanning path with T=X. Each path adjacency must occur in R0 (in some direction), since adding edges cannot join previously separate undirected components. A round-1 row cannot point to both path neighbors, or round 2 adds a chord. The original path orientations must have an endpoint without non-loop in-edges: an in-arrow at the first endpoint forces arrows toward it successively and leaves the far endpoint without one. Starting from an endpoint lacking in-arrows, its original loop forces an immediate back-edge in round 1. To avoid two outgoing neighbors in a round-1 row, each succeeding adjacency is then forced to point backward in R0, except the first. The far endpoint now has an original loop too and forces a second outgoing neighbor at its predecessor, a contradiction including n=3. A bare directed path has a non-target first vertex and yields a round-2 path of diameter n−2, and its last endpoint pair enters at the stated round. At n=1 all relations are fixed. At n=2 there are 16 relations, not the four described in a proof sentence: with no off-diagonal edge the relation is fixed; with two opposite edges the first round adds both loops; with only x→y the first round adds y's loop and adds y→x precisely if x already has a loop, and either resulting relation is fixed. A fresh implementation exhausted 66,066 cases of orders 1–4 (maxima 0,1,2,3), checking the graph-distance and row assertions, and reproduced all 62 paths for n=3–64. Finite checks do not establish the unbounded result. The supplied verify.py was read, not executed.

## originality

PASS

The available prior statements concern static frame properties or counting, usual transitive closure, or a different ternary relation rule. None establishes the sharp synchronous right-Euclidean bound or its post-round-2 radius law. The possibility of coverage in the inaccessible relation catalogue remains explicit.

## value

PASS

This gives the exact round budget for a natural modal-frame consequence operator and reduces the later dynamics on every input to graph distances. The exclusion of the n−1 diameter and the matching path family explain the improvement over a generic reachability bound; this is not an instance census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
