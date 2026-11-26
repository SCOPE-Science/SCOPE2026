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

A geometric fixed point has constant barycentric coefficients on every two-element orbit; its support is a simplex exactly when the union of the positive-weight orbits is a simplex. After moving the three flipped coordinates to the front and choosing the representative with third coordinate zero, the two cross-distance values are a+k and 3-a+k, where a is the two-bit color distance and k is the outside Hamming distance. For distinct orbits their maximum is at most three exactly for different colors with k at most one. The outside cube has no triangles, so every clique lies over a single vertex or edge. An edge block is the join of four pairs of isolated points, hence S^3, and its two attaching fiber tetrahedra are disjoint. Add blocks along a spanning tree first. Each single-fiber attachment wedges on a sphere. Subsequent edges attach along two disjoint contractible fibers: both maps from the resulting two-point homotopy model can be made constant in their connected targets, and its double mapping cylinder adds one S^3 and one loop. The inclusions are simplicial cofibrations, so this gives the stated homotopy type, not only Betti ranks. It includes the boundary n=4, where the base is a single edge. A fresh finite check enumerated the four cross-distances of each pair of original orbits and oriented clique boundaries over Q at n=4,5,6,7; the Betti pairs were (0,1), (1,4), (5,12), (17,32). These computations alone neither certify integral torsion nor identify homotopy; the gluing proof does. For the supplied mod-two check, the inspected replay entry point is python3 check_fixed.py in the frozen package.

## originality

FAIL

Two distinct indexed records state the same geometric fixed-space result, and one explicitly contains it in a stronger statement. The base cube, inclusive scale, exactly three flipped bits, and entire wedge multiplicities agree. This is demonstrated catalogue coverage, not a claim of published priority or independent discovery; the matching entries are in a later date directory and their relationship to the frozen record is not established. The ambient literature cited by the frozen record does not itself give this fixed-space theorem.

## value

FAIL

The geometric fixed-space homotopy type is a natural invariant with genuine information beyond ambient homology, and its proof explains the two sphere dimensions. However, for acceptance of this frozen claim as a distinct exact invariant, the whole formula and model are already covered in a distinct indexed result, which also computes additional cases and a face vector. No distinct refinement survives within the frozen finding. This is not a judgment that the mathematical invariant lacks interest.

The dated certificate retains the supplied scientific assessment, sources and limitations.
