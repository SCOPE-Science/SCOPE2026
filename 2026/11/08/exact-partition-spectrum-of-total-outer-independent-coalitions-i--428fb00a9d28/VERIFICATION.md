---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For r>=3, independent vertex sets lie inside one part; a TOIDS is exactly a set whose complement lies in one part, since it contains every vertex of at least two other parts and is automatically total dominating. In a two-block partition neither block may be pure in one part, and subtracting each unique forbidden pure block from the 2^(N-1)-1 unordered nonempty bipartitions gives c2. With three coalition blocks, at least two complement classes must be pure and in distinct parts, which is also sufficient. Selecting their two nonempty subsets gives sum_{i<j}(2^ni-1)(2^nj-1), while the one r=3 all-pure partition is triple-counted and needs subtraction by two. Four or more blocks force every block outside any coalition pair into one part and leave an impossible coalition partner; source proof covers these cases and the coalition-graph distinction. Independent brute-force adjacency-mask TOIDS/set-partition enumerations agreed for profiles (1,1,1),(2,1,1),(2,2,2),(3,2,1), including the reported (22,25) for K2,2,2. Finite enumeration corroborates only.

## originality

PASS

The original TOI-coalition paper gives the predicate and several scalar extremal numbers. The October 13 complete-multipartite theorem already proves maximum block number three using the same TOIDS characterization, so that maximum is explicitly NOT treated as novel. The submitted result determines exact labelled partition counts at both possible sizes and full pure-block/coalition-graph types, which the complete earlier scalar proof does not entail as a stated result.

## value

PASS

All admissible partitions of a natural domination-coalition graph class are classified, and both nonzero coefficients and coalition graph types are explicit for arbitrarily many unequal labelled parts. A complete count of all witnesses refines the known scalar extremum in a motivated, reusable manner rather than merely recomputing its maximum or an arbitrary restricted slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
