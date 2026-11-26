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

The parity coloring makes GP(8,3) bipartite. The incidence nullspace has dimension nine; any even six-edge subgraph must be one 6-cycle because a simple bipartite graph has no cycle shorter than four. Independent code row-reduces the incidence matrix and enumerates the 512 even subgraphs in free-edge coordinates, finding exactly 24 words of weight six. Exact direct character sums give the seven reduced counts 33,168,160,96,30,24,1 at -8,-4,0,4,8,12,24; on the full dual each occurs in 2^15 extensions. This gives rank 11,534,336, nullity 5,242,880 and visible condition number 24/4. Inverting the nonzero indicator by direct character sums independently gives all nine stated projector numerator counts and absolute sum 3936, with scaling 1/512 on the cycle space and zero off it. Each endpoint convolution norm equals the kernel's absolute sum by a column delta or an aligned row sign. Averaging any real or complex projection onto the invariant range preserves its image and its action as identity on that range; it cannot increase the norm and yields the unique translation-equivariant projection (diagonal in one-dimensional character spaces). Hence the endpoint optimum is unrestricted.

## originality

PASS

The graph, its girth and its 24 hexagons are known: the count follows immediately from Potočnik–Vidali's six girth cycles per edge. The distinct contribution supported here is the full signed switching-class histogram for the weight-six shell, its recoverable range, and the exact 123/16 minimum endpoint projection norm. The inspected stronger cycle classification and close indexed comparisons do not give these character or projection tables.

## value

PASS

For a natural symmetric cubic graph, all shortest-cycle flips define a canonical local measurement operator without arbitrary selection of faces. Its signed table precisely distinguishes lost and recoverable modes (11/16 are recoverable), while the endpoint projection constant measures the best possible linear extraction of that recoverable space, not just its dimension. Both serve as exact benchmarks for comparisons across girth-six graphs. Merely recounting the already-known 24 hexagons would not have this value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
