---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For G=P4 Cartesian C4 (open four rows, periodic four columns), 16 vertices and 28 distinct edges, an independent Python reconstruction generated exactly 21,497 matchings including empty, with face counts 28,306,1672,4863,7416,5470,1620,121 by dimension 0..7. The first-available-edge greedy matching has 10,723 matched face pairs and exactly 1 critical vertex, 12 critical 4-cells and 37 critical 5-cells. Independently built the complete oriented nonempty Hasse incidence graph (107,288 incidences), and topological sorting visited all 21,496 vertices, establishing true acyclicity. Recalculated each signed gradient-path Morse boundary from the actual attached verify.py algorithm and boundary.json: 12x37 matrix, 108 nonzero entries, rank exactly ten, two explicit independent left annihilating rows and a determinant-minus-one 10x10 minor, Smith factors ten 1s. Because the 4-skeleton is a wedge of 4-spheres and pi4->H4 is an isomorphism there, these unit integral attaching columns cancel homotopy-theoretically, leaving 2 S4 and 27 S5. Mod-two homology alone would not exclude integral torsion. The full certificate for this one finite graph was independently replayed; no all-cylinders assertion is inferred.

## originality

PASS

Qualified PASS: P4xC4 is a four-row square cylinder and is not the open P4xP4 square grid (known 6 S4 + 2 S5), the 3-row pentagonal cylinder P3xC5 (known 24 S4 + 3 S5), or the five-column four-row cylinder. Primary open-grid results treat different graph families. No matching full integral homotopy classification for this exact boundary identification was found.

## value

PASS

Closing the four columns of the smallest nontrivial four-row rectangular grid changes the matching complex into a new mixed-dimensional integral wedge with a nonzero 4/5 cellular attaching map; exact torsion-free homotopy classification of this geometrically natural benchmark is a worthwhile finite invariant, independent of general recurrences.

The dated certificate retains the supplied scientific assessment, sources and limitations.
