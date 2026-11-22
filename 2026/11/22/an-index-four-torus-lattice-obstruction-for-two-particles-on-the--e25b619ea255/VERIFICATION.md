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

## Reproducibility

The bundled `verify_rook_tori.py` is a standalone exact-integer checker requiring Python 3 with SymPy. Run it in the same directory; it does not read outside files, use a network, or rely on any external precomputed matrix.

It rebuilds the nine-vertex graph, 36 zero-cells, 126 one-cells and 99 two-cells; checks boundary squared zero and computes the second-boundary Smith form (80 ones and one 2). It enumerates all simple cycles and 78 disjoint cycle pairs, then independently regenerates product torus chains. It verifies 18 triangle-square classes, 6 triangle-triangle classes, the mixed Smith factors (16 ones and two 2s), the exact maximal minor -4, an integral primitive unit minor +1 after adding triangle-triangle tori, and the sufficiency of one row-pair plus one column-pair class.

Success lines include `ROOK_P9_TWO_PARTICLE_INTEGRAL_TORUS_LATTICE_OK` and the declared integral quotient. A finite calculation proves this finite-graph statement because the cubical model exhausts the 2-dimensional configuration space. It does not prove any infinite-family extrapolation or constitute independent external validation.
