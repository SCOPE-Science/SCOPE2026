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

# Reproducible checks and limitations

The exact proof classifies all pairwise intersections of the \(2n2^n\) facet inequalities, then uses Frobenius normal inner products to compute the interior angles. The standalone `verify_ridges.py` generates the signed-permutation vertex matrices and facet normals. It computes the affine dimension of each intersection by a vertex-rank calculation without using the claimed ridge class to determine that dimension.

Executed exhaustive facet-pair tests:

- \(n=2\): 8 vertices, 16 facets, 120 pairs, 32 cross-family ridges and no others.
- \(n=3\): 48 vertices, 48 facets, 1128 pairs, 384 orthogonal-normal ridges, 288 cross-family ridges, 72 same-support ridges.
- \(n=4\): 384 vertices, 128 facets, 8128 pairs, 3072 orthogonal-normal ridges, 2048 cross-family ridges, 256 same-support ridges.

Every comparison matched. Execute `python verify_ridges.py` with NumPy installed. These finite tests mechanically recompute low-order face ranks but cannot replace the all-order geometric proof. The reported result does not establish exact areas, solid angles, intrinsic volumes or historical priority; no independent mathematical audit has been performed.
