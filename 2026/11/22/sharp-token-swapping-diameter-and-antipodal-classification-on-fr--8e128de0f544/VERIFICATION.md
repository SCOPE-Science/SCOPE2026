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

Use a common labelling relative to the identity. If the cycle through the hub contains h leaves, and the q nontrivial leaf-only cycles use s leaves, hub transpositions realize those cycles using h+s+q swaps: a hub cycle takes h, and a leaf cycle of length l takes l+1 by bringing the hub in and out. Since q<=s/2 and s<=2t-h, the upper bound is 3t. Equality requires a fixed hub and t disjoint leaf transpositions. A within-petal pair makes the constructive upper bound at most 1+3(t-1). Conversely, for a matching across petals, every component of the used-edge support is invariant under the permutation. Every matched pair joins distinct components of the graph after hub deletion, so its endpoints' support component must contain the hub. These pairs cover all leaves, giving connected support. Each newly joining support edge merges two current permutation cycles, so any factorization of a permutation with c cycles on n vertices has at least n-1 merges; the cycle-count change gives length at least n+c-2. Here n=2t+1 and c=t+1, hence 3t. Cyclically pairing a_i with b_(i+1) realizes the bound for every t>=2. The count is inclusion–exclusion over the t forbidden petal pairs (with empty matching counted as one); dividing state–antipode incidences by two counts unordered pairs. The generators are distinct odd transpositions and contain the generating star: this verifies degree, bipartiteness, connectivity and the equal radius/diameter by token relabelling. At t=1 all transpositions are edges, and a 3-cycle takes two swaps. Separate byte-permutation BFS and recursive matching generation (`python -B /workspace/independent_replay.py 5`) reproduced diameters 2,6,9,12, and full farthest-state set equality at t=2,3,4 (counts 2,8,60). It is finite corroboration only. Frozen checker.py and its recorded output were read, not executed.

## originality

PASS

The credited finding is the exact friendship-windmill diameter and complete extremal permutation characterization after adding the peripheral matching, not the star upper bound, a connected transposition-factorization lemma, or the abstract matching count. The strongest retrieved comparisons address trees or different two-graph hypotheses, and do not give that characterization. Some cited full texts and the catalogue search were unavailable; that does not establish the absence of prior coverage.

## value

PASS

The windmill is a natural non-tree extension of the star with 50% more swap edges. Knowing that the worst-case number of swaps does not improve, and precisely which token assignments resist any improvement, is information not supplied by monotonicity or an upper-bound comparison. The result identifies articulation and cross-petal structure as the extremal obstruction and provides the exact census, rather than a slight quantitative improvement or a table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
