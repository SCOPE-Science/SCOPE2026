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

Independence gives at most one selection per rung. An empty endpoint or a pair of consecutive empty rungs leaves a vertex undominated. Between successive occupied rungs with no empty rung, independence forces opposite selected rails; across a single empty rung, domination of both vertices on that rung forces the same alternation condition. These three conditions are also sufficient. A first-rail choice and the z=n−k one-vacancy gaps among p=k−1 gaps therefore encode the states exactly. Since n≥2 requires k≥2, a vertical flip breaks alternation with at least one neighboring occupied rung, by independence or by domination according as the gap has size zero or one. A horizontal slide preserves feasibility exactly when it transfers a vacancy across an internal selected rung into an empty gap, hence swaps adjacent 01 and 10 and preserves the first-rail choice. This proves the two path-token components, including z=0,p. For their metric, sorted tokens cannot pass. Moving all left-going tokens in increasing order and then all right-going tokens in decreasing order attains the sum of absolute displacements; target positions are strictly increasing, so no intervening token blocks those moves. Opposite packed configurations attain z(p−z). Coordinatewise medians are strictly increasing and are the unique tuple in all three pairwise metric intervals. Each consecutive gap pair contributes binom(p−2,z−1) edges per copy in the nonsaturated range. Summing the binomial counts gives the two stated series (subtracting the n=1 term for vertices). At minimum size, z=p for odd n and z=p−1 for even n, yielding the stated singleton and path cases.

## originality

PASS

Bounded pass for the all-cardinality structure theorem for the open ladder as a seed, especially the exact two-copy isomorphism and preservation of a first-rail phase under every legal slide. The unweighted maximal-independent-set count, known path-factor examples and standard grid/lattice metric consequences are not independent originality claims. The closest circular-ladder result uses a related gap construction but does not cover this open-boundary state space or all feasible open-ladder cardinalities.

## value

PASS

The result identifies every fixed-size state graph of a natural and widely used seed, not just its independent domination number or total static count. The explicit coordinate map decides reachability, constructs shortest legal sequences and identifies the exact obstructions to crossing components. This is a useful structural classification; the older Fibonacci total and standard consequences for path-token factors are not by themselves the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
