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

Cut vertices are forced since omission leaves an entire component beyond reach of a connected dominating set. In the cut-vertex case leaves are optional, with selected leaves deletable. The block-cut tree precludes an outside path joining distinct vertices of a cycle block; a connected selection therefore leaves at most one cyclic omission interval. An interval of length three would leave its middle noncut vertex undominated. The choices empty, singleton or consecutive noncut pair are independent across cycles, and inclusion-minimality takes maximal omissions: all pairs and exactly the singletons isolated within the induced noncut paths, with empty permitted only if there are no noncut vertices. All supersets of a CDS remain connected and dominating, so there is no hidden multivertex-deletion issue. The size enumerator multiplies. Two distinct equal-size pair omissions have symmetric difference two exactly when the free-path edges overlap; singleton omissions form a clique. A pair and an isolated singleton are disjoint and differ in three vertices. Every changed coordinate costs at least two in symmetric difference and the coordinates are disjoint, so a swap changes exactly one coordinate. Components and diameters of the Cartesian product follow. In a bare cycle the maximal omissions are pairs and the exchange graph is the line graph of the cycle (including the triangle); K_1, K_2 and trees give the stated separate cases.

## originality

FAIL

The prior cactus all-CDS result states the full labelled blockwise choice family with independent coordinates, not just a cardinality polynomial. Passing to maximal local omissions gives the exact minimal family and enumerator, and applying the distance-two rule to that product gives the entire asserted exchange graph by elementary direct implication. This is substantive coverage by a stronger result, not an assertion that the prior paper writes the same exchange formula.

## value

FAIL

The exchange question is natural and the formula is convenient, but here it is mechanically implied by the known independent labelled cactus choices: take maximal omissions, then connect local choices by one swap. The component counts and diameters have no additional structural content beyond that product. No scientifically distinct valuable claim survives as a repair of the frozen result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
