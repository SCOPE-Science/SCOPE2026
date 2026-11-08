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

The accompanying `verify.py` constructs categorical-product edges directly, enumerates independent sets and legal token slides, and checks the full adjacency spectrum, number of vertices and edges, connectivity and bipartiteness for nine two-token profiles. There are 605 labelled two-token states across these cases. It checks the exact spanning-tree formula by *integer* Laplacian cofactor determinants for the \((3,3)\) and \((3,4)\) cases, and compares floating logarithms of eigenvalue products with the exact formula as an additional independent arithmetic check for small graphs. Eleven higher-token profiles are checked for isolation and the stated labelled-state count. The structural proof, not finite experiments, establishes the general statement.

Run under Python 3 with `numpy`, `networkx`, and `sympy` installed: `OPENBLAS_NUM_THREADS=1 python verify.py`. The expected successful output begins `VERIFY_OK` and includes `exact_tree_checks= 2` and `frozen_profiles= 11`.

The independent audit status in the front matter remains unperformed; no external certification is asserted.
