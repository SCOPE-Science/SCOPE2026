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

For a cubic graph, a proper coloring is strong odd exactly when each color class is independent and no open neighborhood meets it twice. The LCF edges give 36 edges, cubic degree and girth seven (computed by shortest paths with one edge deleted). Independently enumerating independent subsets and applying the neighborhood filter gives 1,196 admissible nonempty classes. For a fixed remaining vertex mask one can pick any deterministic pivot in it and branch over all wholly remaining classes containing that pivot; every completion has a unique such class and is reached exactly once. This gives 0,0,0,0,1304 partitions for k=1..5. The resulting set agrees with both frozen lists and contains the stated witness. Sorting sizes yields the six counts 16,48,96,336,400,408 in the reported order. The 32 automorphisms are exactly the bijections preserving the graph-distance matrix (distance one is adjacency); backtracking with pairwise distance constraints gives the full group. Its action on partitions gives orbit multiplicities 5,19,30 for sizes 8,16,32. Exactly 320 partitions have three distinct colors in every open neighborhood, hence are proper square colorings; the complement is 984. Five occupied named colors multiply the unnamed count by 120. The supplied search and exact-cover code were inspected, not run.

## originality

PASS

The supported distinct finding is the complete strong-odd optimum census for the specified McGee graph, including profiles, orbits and the square subset. The graph definition, automorphism order and strong-odd definition are not discoveries. Neither the inspected sparse-coloring bounds nor the closely related catalogue entries cover the exact claim.

## value

PASS

The unique cubic girth-seven cage is a natural benchmark rather than an arbitrary sampled graph. The census resolves both the optimum and its multiplicity modulo two meaningful symmetries (color names and graph automorphisms), and measures how much larger the strong-odd family is than the distance-two family at the optimum. These exact benchmark data are substantively useful even without a theorem for all cages.

The dated certificate retains the supplied scientific assessment, sources and limitations.
