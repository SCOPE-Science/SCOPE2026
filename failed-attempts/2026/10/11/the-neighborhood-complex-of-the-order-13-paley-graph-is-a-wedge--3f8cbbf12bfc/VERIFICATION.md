---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For P13 with quadratic-residue steps {1,3,4,9,10,12}, direct reconstruction of all 13 open neighborhoods gives exactly 598 nonempty faces, f-vector (13,78,221,195,78,13). An independently written bit-mask matching with pivots 0,...,12 makes 286 disjoint cover pairs, leaves one critical vertex and 25 critical triangles, and topologically sorts all 598 vertices of the 2067-arrow oriented Hasse graph. Forman discrete Morse then gives one zero-cell and 25 two-cells with constant attaching maps, hence an INTEGRAL homotopy equivalence to wedge^{25} S^2; mod-p ranks alone are not used to infer homotopy.

## originality

FAIL

A DISTINCT published finding states the exactly identical open-neighborhood-complex homotopy theorem for precisely P13, with the same f-vector (13,78,221,195,78,13) and an independent complete Morse matching. Exact identity of mathematical statement, not title resemblance, decisively destroys originality; the other source also determines chromatic number 5. A separate proof with a different pivot order cannot restore originality to the submitted claim.

## value

PASS

The homotopy type of the canonical P13 Paley graph common-neighbor complex is an intrinsically meaningful integral invariant with an explicit topological obstruction to coloring. An exact full homotopy answer, beyond Betti ranks, is valuable AS mathematics even though the submitted claim is not original because another published proof already supplies it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
