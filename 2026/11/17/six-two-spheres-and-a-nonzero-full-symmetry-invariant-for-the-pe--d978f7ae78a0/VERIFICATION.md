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

For C10^2 with 20 edges, exact enumeration of perfect matchings yields 22 five-edge facets and 457 nonempty faces, with face counts (20,115,190,110,22); ordinary matching complex has additional nonextendible faces and is not interchangeable. An independently implemented lexicographic edge-mask discrete Morse matching leaves one 0-cell, one 1-cell and seven 2-cells (224 matched pairs); oriented Hasse DAG contains all 457 nodes and is acyclic. Independent integer gradient expansion yields the precise 2-to-1 Morse boundary (-1,-1,0,0,-1,0,0), containing a primitive unit attachment. The one-cell with one 2-cell cancels, proving integral wedge of six 2-spheres and nonshellability in a pure four-dimensional complex. Independent signed Lefschetz enumeration of all 20 dihedral symmetries gives rotations (6,-1,1,-1,1,4,1,-1,1,-1) and reflections (2,0,2,0,2,0,2,0,2,0); average 1, matching rational D10 fixed-rank one. These computations exhaust a single ten-vertex complex, not all antiprisms.

## originality

PASS

Distinct perfect-matching complex and full-dihedral character for C10² not covered by ordinary C10² matching or perfect-matching C12² results; cyclic ladder papers concern cubic rather than four-regular antiprism graphs.

## value

PASS

Perfect-matching extendibility makes a natural but different subcomplex of the well-studied ordinary matching complex. Its surprising pure-dimension-four yet 2-sphere wedge type, nonshellability and exact nonzero full-dihedral invariant provide a useful finite integral and equivariant benchmark, especially contrasted with the closely studied twelve-vertex antiprism.

The dated certificate retains the supplied scientific assessment, sources and limitations.
