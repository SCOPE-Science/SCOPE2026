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

The facets in the actual claim are complements of disconnected induced five-sets in the cycle-plus-antipodal-rungs graph, not complements of independent sets. All facets have dimension 2n−6. I independently generated them by a set-frontier search on each five-set and propagated faces down by cardinality. I reconstructed the vertex-stage matching by simultaneous disjoint toggles at each vertex and rechecked the entire reversed-matching Hasse orientation with a sink-elimination sort, obtaining complete visitation in all five cases. Facet counts are 8,152,672,1862,4208; nonempty face counts are 32,522,3175,14765,62850. The orientation counts are 56,1990,16944,98056,491376. The unmatched faces consist of one vertex in each case and respectively 1,41,216,582,1213 cells in degree 1,4,6,8,10. Each pair is a codimension-one incidence; the vertex-stage toggles are disjoint within a stage and matched faces are deleted from eligibility thereafter. Thus the finite acyclic matching theorem gives a homotopy-equivalent CW complex with exactly the unmatched cells. There is no other positive-dimensional skeleton below the stated degree, so the attachments give a wedge of spheres, including the circle case for n=4. The recorded mod-two computation is corroborative, not the basis for the homotopy conclusion.

## originality

PASS

The distinct claim is the five specified ordinary five-cut integral homotopy types. Direct same-graph comparisons use other cut parameters, or the total convention; broader statements with the same cut parameter concern open two-row ladders, without the two twist-closing edges. The strongest primary sources inspected establish the framework or pose the direction, but do not give these homotopy types by specialization.

## value

PASS

The object is a canonical twisted ladder family and the cut-complex topology is explicitly motivated in the primary ladder literature. After the known ordinary three- and four-cut classifications, the next cut parameter changes the picture at the start of the stated range: the pure Wagner-graph complex is a circle, whereas the next four sizes are top-dimensional integral sphere wedges with specific ranks. The boundary example rules out unqualified top-dimensional-wedge behavior and the consecutive exact ranks give concrete tests for a structural five-cut theorem. The value is this finite boundary pattern and its integral homotopy verification, not an extrapolation or a special mathematical role for the upper computational cutoff eight.

The dated certificate retains the supplied scientific assessment, sources and limitations.
