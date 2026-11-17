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
# Verification of the exact tetrahedron-volume profile

Run `python3 check_hull_tetra.py` with Python 3; no third-party packages are required. The attached file produces the exact result

```
CUBE_OCTAHEDRON_HULL_TETRAHEDRA_EXACT_PASS vertex_quadruples=1001 bernstein_nonnegative=8008 class_tight_counts=2,48,12,8,12 cube_maxima=2 axis_corner_maxima=8 three_vertex_overlap_pairs=0
```

The program constructs every unordered quadruple of the six axial and eight cube vertices; computes its signed determinant polynomial in \(h\); selects one of the five sharp polynomial envelopes based on the number of axial points; and verifies exact nonnegative rational degree-three Bernstein coefficients for each sign on the full closed interval \([1,3]\). A Bernstein polynomial with nonnegative coefficients is nonnegative throughout the interval, giving rigorous exhaustive bounds for uncountably many real parameter values. Independent constant and sharpness checks recover all exact classwise optimizer counts. It also constructs and compares the two cube and eight mixed extremal vertex sets and verifies no pair shares three vertices.

The mathematical argument in `RESULT.md` separately justifies the vertex classification, affine-to-vertex reduction, exclusion of nonvertex maximizers, the cube and octahedron parameter regimes, polytope-volume decompositions, and the monotonicity needed for the unique normalized optimum. No numerical random sampling, timeout, or failed search is treated as a proof. Independent audit and independent certification were not performed.
