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

Permuting the symbols is transitive on each of the two edge forms, and graph-triangle membership distinguishes them. The independent exact replay is /workspace/branches/7668909b-2f63-4187-abb8-d9a671040f7a/rips_replay.py with run output rips_replay.out in the same directory; the frozen verify.py was inspected, not executed. The replay builds each fault graph before BFS and tests all 4,095 nonempty vertex subsets. There are 12 isolated points below radius one. At one the connected graph remainders after collapses have cycle ranks 3 and 2. At two the face vectors (12,40,42,10) and (12,37,38,10) collapse to two-dimensional cores of (12,32,24) and (10,23,16). I checked that the replay uses current free faces and actual oriented boundary words after collapsing a spanning tree; singleton relators kill all 21 and 14 generators. A simply connected two-complex is a wedge of two-spheres by Hurewicz and homological Whitehead, with ranks 3 and 2 from these Euler characteristics. At radius three the triangular case collapses in 1,151 pairs; the reversal case collapses at three and four in 543 and 1,535 pairs. At diameters 4 and 5 the complexes are simplices; integral graph distances settle all real threshold intervals. The intact signed boundary ranks are 31 and 12 on a 48-generator C₂, and the 3-boundaries have unit invariant factors. For each inclusion the replay uses an integral kernel basis and appends its embedded cycles to the intact 3-boundaries. The resulting matrices diagonalize over the integers with nonzero diagonal entries all units and ranks 15 and 14. Thus B₂(intact)+Z₂(fault) is saturated in C₂(intact), hence in Z₂(intact); its image modulo B₂ has rank 3 or 2 and free quotient. Since the fault H₂ groups are free of the same ranks, the maps are injective with free cokernels of ranks 2 and 3 in Z⁵. This is a stagewise homotopy classification plus the two scale-two maps, not a classification of all interscale maps.

## originality

PASS

The distinct result is the complete stagewise classification for all single graph-edge faults on the truncated tetrahedron with recomputed distances, and the two integral primitive maps into the intact stage. The intact graph and same-vertex Euclidean result are prior; the graph-specific fault data and actual maps are not implied by either. The closest same-day method match is on a different graph.

## value

PASS

Both edge orbits are natural symmetry classes of a standard Archimedean graph, and all 18 single faults are covered. The scale-two integrity result distinguishes the number of surviving two-dimensional classes and shows that no nontrivial torsion obstruction is hidden in the quotient of the intact lattice. Neither rank-only stability nor the intact classification could answer those questions. This is a useful exact finite benchmark for graph-metric persistence under edge damage; it does not depend on claiming a general robustness theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
