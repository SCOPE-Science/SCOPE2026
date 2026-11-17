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

# Reproducibility and scope

Execute `python3 check_tetrahedra.py` from the directory containing this document. The program requires only Python 3's standard library. It generates the exact twelve icosahedral coordinates, thirty midpoint vertices and twenty triangular faces, checks all 27,405 unordered four-subsets by two integer-pair determinant formulas, compares algebraic values without numerical tolerances, and independently constructs 120 symmetry permutations from ordered facial bases.

Checks include the sixty maximizing tetrahedra, 240 second-level vertex tetrahedra, 27 distinct determinant levels including zero, exactly twenty continuous maximizing facial families, unique maximizing replacement position in each extremal vertex tetrahedron, the three moving points of each facial family, and the long-anchor equilateral side \(\varphi^2\). The complete finite spectrum is separately recorded in `spectrum.csv`. The proof that these finite checks settle the global continuous maximum is the multilinear convex-combination argument in RESULT.md.

The reported verification assesses this exact finite certificate and its accompanying proof. It does not constitute an independent audit, and it makes no claim about unstated variants, unindexed literature, or all continuous tetrahedral volumes.
