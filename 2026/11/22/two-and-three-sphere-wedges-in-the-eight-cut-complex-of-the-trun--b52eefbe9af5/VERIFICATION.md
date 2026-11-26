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

Independently reconstructed the 12-vertex graph as four triangles joined by six specified matching edges and enumerated all 495 candidate complementary tetrahedra by induced component merges. The resulting face vector is (12,66,204,252); each of the 16 missing triangles has an explicit cone filling in the two-skeleton. With the complete one-skeleton, all triangular edge loops normally generate the fundamental group, so these fillings give simple connectivity. Independent exact Smith computations gave 55 ones for the second boundary and 143 ones for the third, with zero remaining invariant factors and zero boundary composition. The image of the third boundary is primitive in the second chain group and hence in the second cycle lattice. The two-skeleton is equivalent by Hurewicz and Whitehead to 149 two-spheres. The full complex is the homotopy cofiber of a map from a wedge of 252 two-spheres into this wedge; its degree matrix represents the third boundary into the cycle lattice. The integral basis changes are realized by homotopy self-equivalences of the two wedges, and the resulting identity blocks cancel while the zero blocks yield six two-spheres and 109 three-spheres. Purity follows from the equal-size facets, and nonvanishing H2 over every field obstructs Cohen–Macaulayness (and thus pure shellability).

## originality

PASS

The inspected closest literature and indexed findings do not state or imply the ordinary eight-cut homotopy type. The identical indexed result is a copy of the assigned finding, not a distinct result; distinct same-graph records concern different cut parameters or the total-cut construction. This is a best-of-knowledge conclusion, not a global priority certification.

## value

PASS

A canonical cubic polyhedral graph gives a natural test of ordinary cut topology beyond the existing three- and four-cut calculations. The precise integral homotopy type in this small-dimensional regime supplies a concrete pure cut complex with homotopy in two different positive dimensions, hence an explicit obstruction to shellability and Cohen–Macaulayness; an Euler characteristic, mod-two rank, or a generic complete-skeleton calculation would not establish that information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
