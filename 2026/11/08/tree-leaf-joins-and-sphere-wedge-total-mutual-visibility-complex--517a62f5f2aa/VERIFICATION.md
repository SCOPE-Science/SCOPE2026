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

# Reproducible numerical corroboration

Run `python verify_tree_rook.py` with a standard Python installation; no extra libraries are required. The program generates labeled Cartesian products from their graph adjacencies, computes every graph distance by breadth-first search, enumerates shortest-path DAGs, and tests actual visibility against the proposed leaf-layer criterion. It checks all feasible and maximal configurations for the stated parameter choices, verifies the generating functions, and tests separate internal-layer singleton obstructions. It further calculates reduced mod-two homology by Gaussian elimination of simplicial boundary matrices for three cases. Actual output:

```text
PASS tree_vertices 3 leaves 2 n 2 boundary_masks 256 valid_faces 81 geodesic_tests 4 path_variants 2
PASS tree_vertices 3 leaves 2 n 3 boundary_masks 4096 valid_faces 324 geodesic_tests 12 path_variants 2
PASS tree_vertices 4 leaves 2 n 2 boundary_masks 256 valid_faces 81 geodesic_tests 4 path_variants 2
PASS tree_vertices 4 leaves 3 n 2 boundary_masks 4096 valid_faces 729 geodesic_tests 6 path_variants 2
PASS tree_vertices 5 leaves 3 n 2 boundary_masks 4096 valid_faces 729 geodesic_tests 6 path_variants 2
HOMOLOGY_PASS n 2 leaves 2 faces 81 top_betti {3: 1}
HOMOLOGY_PASS n 3 leaves 2 faces 324 top_betti {3: 4}
HOMOLOGY_PASS n 2 leaves 3 faces 729 top_betti {5: 1}
VERIFY_OK cases=5 boundary_masks=12800 all_shortest_paths=PASS face_polynomials=PASS forbidden_interior_singletons=PASS mod2_homology=PASS
```

The computation is exhaustive **within** each tested finite graph; it does not prove the unrestricted tree/product theorem, integral homotopy, or publication priority. Those follow from the separate symbolic argument and literature comparison. An independent audit has not been performed.
