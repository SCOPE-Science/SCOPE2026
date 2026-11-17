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

# Reproducible checks

Run `python3 verify_latin_homotopy.py` using standard Python 3.10+. It needs no external files or packages. Compare its complete terminal output with `verify_latin_homotopy_output.txt`. The final line should be `VERIFY_OK_LATIN_HOMOTOPY_FINITE_CHECKS`.

The independent graph enumeration constructs every adjacency from row, column and symbol equality, lists maximal cliques, expands all faces, counts intercalates and verifies the unique free-facet property. It computes mod-two simplicial homology ranks by exact elimination for cyclic group tables of orders 2 through 6, the Klein four-group table and a nongroup order-five square. All seven tested cases have predicted free two-dimensional Betti ranks, no mod-two homology in other positive dimensions.

This is finite corroboration, **not** an infinite homotopy proof. The uniform proof is in `RESULT.md`, using the cover nerve of the line core, rainbow-triangle attachment correspondence, free-face collapse of each intercalate tetrahedron, Euler characteristic, Hurewicz and Whitehead. No higher homotopy groups or symmetry-module structures are separately determined. Independent mathematical audit has not been performed.
