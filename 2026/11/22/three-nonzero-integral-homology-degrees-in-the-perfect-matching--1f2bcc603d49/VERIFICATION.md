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

The face complex contains exactly the nonempty submatchings of the perfect matchings, plus the empty face. A new row-sweep domino enumerator and submask enumeration recovered 281 facets and the entire stated face vector (511,338 nonempty faces). The edge-pivot matching gives only legitimate disjoint codimension-one pairs: at each pivot, a face belongs to at most one candidate pair. Independent depth-first cycle detection on the full oriented cover graph checked all 511,338 vertices, and found 255,663 pairs with 1,2,8,1 critical cells in degrees 0,3,4,5. Integral signed boundary accumulation in reverse topological order gives the reported 2×8 matrix with unique entry −1 at the first row/column and zero 8×1 matrix in degree five. Each substitution uses the signed incidence unit and the other boundary faces, with paths terminating by acyclicity. The unit entry kills one direct summand without torsion. Forman's acyclic matching theorem gives a homotopy-equivalent CW model with one vertex and no 1- or 2-cells, implying 2-connectivity by cellular approximation. Thus the listed reduced integral groups are complete; the vanishing cellular degree-five boundary does not determine the attaching map.

## originality

PASS

No identified earlier distinct result supplies the complete integral homology or an implying homotopy classification for this four-row grid. The same-width neighboring instances, the full three-row family and ordinary matching-complex data have different hypotheses.

## value

PASS

This is the next even-column instance of the first wider rectangle family beyond the three-row theorem, following 4×4 and the neighboring 4×5 result. Its three consecutive integral degrees distinguish it from the three-row single-degree pattern and the smaller same-width cases. The complete torsion and connectivity information is useful when testing candidate grid homotopy formulas, and is not mechanically available from the facet count or Euler characteristic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
