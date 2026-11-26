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

In the full binary order-(k−1) de Bruijn graph the frozen potential p is minus the position of the first 1, with p=0 on the all-zero vertex. Each edge has increment at most one: shifting a later first 1 decreases its position by one; in the remaining cases the initial potential is zero. Summing over one copy of the required arcs using in/out degrees gives deficit −(F_k−1): for each 1≤j<k−1 there are F_{k−1−j} admissible vertices with j initial zeros and terminal 1. The unmarked arcs on a cyclic walk must make up the deficit, even if they contain 11. The copies of 0x0 with legal nonzero x cancel the degree imbalance, and routes via the all-zero vertex give strong connectivity. The augmented Euler circuit proves attainment with no cyclic 11, including k=2 when no copies are needed. Independent BFS in the full graph returned lengths 3,6,10,17 at k=2,3,4,5. Replay by starting at (zero suffix, empty required-edge mask), allowing both appended symbols and updating the mask, until the zero suffix is first reached with full mask; any feasible cycle can be rooted there because it contains the required all-zero edge. The BFS proves those orders only.

## originality

FAIL

The strongest distinct catalogue match states the same legal optimum and repeat multiset, and its proof already gives a certificate on the full host graph. The added quantifier over unrestricted hosts is correct but a direct implication of that certificate, not a new solved case requiring a new argument. This is a mathematical comparison, not a priority inference from archive dates alone.

## value

FAIL

The exact cover overhead and optimal witness would be useful for a natural constrained dictionary. But the same optimum and witness exist in a distinct record, and the only apparent added content is a host-scope expansion already certified by the same one-step shift inequality. It is not a distinct exact result under the value standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
