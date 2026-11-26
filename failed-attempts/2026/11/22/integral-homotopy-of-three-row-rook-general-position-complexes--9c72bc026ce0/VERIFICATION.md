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

In the diameter-two rook graph a forbidden triple consists exactly of the two consecutive legs of a right angle with its nonadjacent endpoints. Double occupancy in column j uses two rows that cannot then appear in any other column, so no second column can have double occupancy. Double-occupancy faces not containing a full column therefore belong to the stated thickening simplex, while a full column is isolated from all other cells. Two different thickenings intersect only in the column-thin complex A_n; the intersection of any individual thickening with A_n is S^0 joined with the nonempty simplex of allowed cells in the remaining columns, hence contractible. Cofibration gluing proves that A_n includes by a homotopy equivalence into the thickened core. Joining three-point spaces, starting with K_{3,3}, doubles the wedge rank and suspends at each stage; the core is therefore simply connected for n≥3 and has 2^n spheres in degree n−1. Each of the n column triangles attaches along its three edges already in the core by a nullhomotopic boundary map. The homotopy pushout splits off n two-spheres relative to the core up to homotopy, so the actual A_n inclusion induces an integral homology summand even at n=3, where the total rank in degree two is 11. Both sides are connected, giving the ordinary H_0 assertion as well.

## originality

FAIL

The exact integral wedge for all n≥3, the n=3 degeneracy, and the split column-thin inclusion are all explicitly covered in the distinct Resultary finding 97746ad05664. Its cofiber conclusion additionally implies the stated degree-two homology quotient. No independent novel remainder appears in the frozen Finding.

## value

FAIL

The column-defect topology and how it sits over a natural core would be a meaningful structural distinction from prior counting alone, but the exact phenomenon, together with a stronger relative conclusion, is already known. The frozen claim does not advance a separate new structural consequence beyond that coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
