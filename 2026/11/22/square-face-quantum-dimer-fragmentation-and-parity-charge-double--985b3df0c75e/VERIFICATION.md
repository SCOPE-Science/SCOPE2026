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

An independent exact reconstruction from coordinates in Q(sqrt(2)) gives 24 vertices, 48 edges, 8 triangles and 18 induced square cycles, precisely the allowed faces. Exhaustion follows by branching on the partner of the first uncovered vertex; checking whether the toggled boundary is another matching gives exactly the allowed transitions. The reconstruction verifies 1088 matchings, 2616 unordered transitions, 69 components with counts 1,6,24,24,14 at sizes 594,16,14,2,1, and six component orbits under the 48 signed coordinate permutations. Binary reduction gives rank 18 and 35 occupied classes: the giant class is connected, and the 3,12,12,7 classes of sizes 32,28,4,2 respectively each split into two equal components. Each legal move preserves the quotient. At v=t>0, the pair blocks sum to t times the graph Laplacian, with one zero mode per component. At v>t>0, each pair block is strictly positive on its endpoints and the common kernel consists of the 14 isolated matchings. There is no claim about the remaining spectrum.

## originality

PASS

Pass for the specific complete square-face component and charge census, especially the uniform splitting of all 34 nongiant classes. The matching count is explicitly credited to earlier work, and the RK kernel statements are consequences of the census, not new operator theory. Inspected structural theorems on surface resonance graphs and adjacent exact classifications do not determine this census.

## value

PASS

For the natural face-only local-move model on an Archimedean solid, the exact component-by-charge census quantifies a meaningful gap: identical conserved linear charges need not permit a legal move sequence, and every smaller class in this model is a precise doublet. The sector sizes, symmetry orbits and number of frozen states are directly useful for block decomposition and exact RK zero-mode counts. The finding does not rely for significance on recomputing the known state count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
