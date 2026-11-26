---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The finding is true, but the frozen proof's insistence on component-size weights in §2 is incorrect. In the incidence cokernel each e_ij maps to the unit generator of its connected component, so the induced augmentation sends each such generator to 1, not to the component size. The sum of original basis elements in a component would map to its size times the unit, not to a basis element. Using the correct unit-weight augmentation gives the natural quotient ker(epsilon)/im(partial_2), which surjects at every stage with free target of rank number of components minus one. For H_2 the mixed triangles are the edges of the incidence graph and each pair of deleted labels has two oriented length-two paths between diagonal vertices. A cycle has zero pendant coefficients and equal coefficients along each oriented path, and the tetrahedron relation identifies the two paths with coefficient a unit. For every pair keep the path via e_ij with i<j; these choices coincide at all stages, so the quotient is naturally the complete-graph integral cycle lattice and the star-tree circuit bases extend. The tetrahedral relations are independent, leaving no higher homology. This reconstruction proves the displayed ranks, splits and barcode despite the erroneous weight assertion. The small independent exact check at (4,5) obtained H_1 ranks (19,12,6,2,0) and H_2 ranks (0,0,0,1,3), with stabilized H_2 basis column (1,0,0).

## originality

FAIL

Best-of-knowledge rejection for substantive prior map-level coverage: the published November 17 Resultary record fac6a09d737e concerns the identical dissociation-complex filtration under successive matching-edge deletions in K_{a,b} and expressly gives coherent integral bases determining every inclusion map, degree-one deaths of integral classes born at zero, and t−2 permanent primitive degree-two births at stage t. This is not a title-only, stagewise or field-only match: the statement describes integral classes and bases with the complete field barcode as a consequence. The frozen record's numerical degree-one multiplicities follow by subtracting the independently credited stage ranks once all births are at zero, and its chosen cycle-lattice presentation does not establish a distinct scientific claim beyond the previously classified maps.

## value

FAIL

The mathematical classification would be useful if new, but the record offers no demonstrated further invariant or application beyond the earlier integral map classification. Its explicit death multiplicities are forced by the earlier behavior and known ranks, and the chain presentation is presented as a proof of the same classification, not a distinct usable result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
