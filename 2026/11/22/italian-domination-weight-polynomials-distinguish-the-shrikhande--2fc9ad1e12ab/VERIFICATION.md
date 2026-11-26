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

For each support A, reject it if any outside vertex lacks a neighbor in A. Otherwise each outside vertex with exactly one neighbor in A forces a double there, and every other outside vertex is defended irrespective of which remaining selected vertices are doubled. The coefficient contribution is thus z^{2|U|}(z+z²)^{|A|−|U|}, where U consists of the distinct forced vertices. A separately written exact implementation exhausted all 65,536 supports per graph, reproduced both full coefficient vectors and returned differences (8,224,1184,1408,1176,832,640,256) at degrees 4 to 11, zero elsewhere through degree 32. Replay: python3 /workspace/branches/d83fa4a7-b104-4079-9700-76c20ad5f04a/reproduce_italian_weights.py; recorded full vectors are in reproduce_full.json in the same directory. The frozen Python and C++ checkers were inspected, not executed. For the optimum structure, 2(16−|A|)≤6w implies w≥4; equality forces four ones, no edges among them, and two neighbors at each outside vertex. In a four-coclique, the outsider neighbor counts have sum 24 and pair-count sum 12 by the common-neighbor parameter 2, giving zero sum of squared deviations from 2. Such a coclique is maximum because it cannot extend (so no larger independent set can contain any four of its vertices). Rook cocliques are permutation transversals. For Shrikhande, the six modular adjacency differences leave exactly the four listed triples extending the origin to a four-coclique, each an order-four subgroup after adjoining the origin. Distinct subgroups have disjoint collections of cosets, and translation brings every four-coclique to one of them. The reproduced independent-set counts, 24 and 16, agree with the weight-four counts.

## originality

PASS

The supported distinct claim is the full labelled Italian weight-polynomial separation and exact high-degree agreement for these benchmark graphs. The rook minimum and all its optimizers are known, and a prior design paper may already classify Shrikhande's maximum independent sets, which would also give its minimum Italian configurations. No independent priority claim for that census is needed for the polynomial finding.

## value

PASS

The rook and Shrikhande graphs are a natural strongly regular benchmark pair with identical basic parameters and the same Italian domination number. Exact labelled enumeration exposes where the refined invariant separates them and where coefficients agree, giving a usable benchmark that is not obtainable from merely comparing minima or distinct subset-domination invariants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
