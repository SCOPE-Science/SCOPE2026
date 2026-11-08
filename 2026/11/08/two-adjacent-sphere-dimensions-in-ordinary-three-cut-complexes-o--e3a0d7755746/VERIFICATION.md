---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and proof boundary

The mathematical proof uses one path triangle per square as a free face of that square tetrahedron, then its now-exposed opposite diagonal as a free edge. Its surviving complex is the two-skeleton of the cube, with extra unattached long edges. The original proof, rather than finite computation, establishes these statements for every dimension at least three.

`python3 artifacts/verify_collapse.py` constructs every dual simplex for dimensions three through six and checks every individual free-face removal and the surviving triangulated cube skeleton. `python3 artifacts/verify_cube.py` independently checks mod-two boundary ranks for the same four dimensions, all degree-two/degree-three boundary compositions, and the full local face characterization in dimensions three and four. Recorded outputs are `artifacts/collapse_check.txt` and `artifacts/boundary_check.txt`. Both programs use only the Python 3 standard library.

Numerical checks over the field with two elements do not establish integral freeness or the homotopy wedge for infinitely many dimensions. Those conclusions instead use the explicit all-parameter collapse, simple connectivity, free integral homology of a two-dimensional simply connected CW complex, integral combinatorial Alexander duality, and the Hurewicz–Whitehead argument in RESULT.md.
