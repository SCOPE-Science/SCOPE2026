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

The repaired RESULT.md preserves the update map and all census statements. The four shapes exhaust three-edge sets on five labels; permutations of the five labels act on their placements and intertwine the update. A pinned update is monotone, and its least initial state S maps above itself. Its iterates therefore increase and obey exactly the bootstrap recurrence, since adding the previously active sites to the next state is then redundant. This proves the newly stated equivalence and the sufficiency of checking S for universal forcing. The four explicit least-state trajectories were checked by open-neighbor threshold counting; the star takes exactly three steps and the others stop short. For independent verification of the arbitrary-start census, construct the pinned functional digraph, peel indegree-zero vertices to isolate periodic states, verify F² fixes every periodic vertex, and traverse backward to assign basin and first-entry depth. The complete independent calculation gives (one, two-cycle, other fixed, max entry) = (128,0,0,3), (98,28,2,2), (124,0,4,5), (94,30,4,4) for star, triangle, path and wedge-plus-edge. Pair counts give 141 and 188 consensus starts respectively in the adjacent and nonadjacent types. The minimum is also verified without the prior scalar theorem by these pair obstructions and monotonicity in added pins.

## originality

PASS

The frozen treatment of the scalar minimum as part of a new forcing result fails the prior-implication check: arXiv:2606.03687v3 Theorem 1.2 already gives three at k=2, and the least-state equivalence transfers that number exactly to fixed-one pinning. The repaired RESULT.md removes the scalar threshold from the contribution, credits it as background, and proves the precise reduction. The surviving claim is the exact arbitrary-start basin and sharp periodic-entry profile by pin shape, including which triples have a full consensus basin and the two nontrivial basin sizes for pairs. Neither irreversible hull closure nor the published unpinned Petersen map supplies those profiles. The repaired claim, not the original attribution, passes.

## value

PASS

The revised contribution measures how stubborn placements alter the fixed-point and oscillation basins and worst transients of a natural symmetric test graph. The census distinguishes two pin shapes with the same number of other-fixed starts but dramatically different oscillatory basins, and separates the shapes that can exhibit oscillation from those that cannot. Exact basins and sharp clocks are useful finite benchmark data for reversible majority under interventions, not a recomputation of the already known minimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
