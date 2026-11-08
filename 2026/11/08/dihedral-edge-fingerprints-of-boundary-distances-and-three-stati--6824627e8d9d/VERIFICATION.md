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

# Reproducibility checks

Run `python check_boundary_pairs.py` with Python 3, NumPy and SciPy. On the tested environment the checker printed `VERIFY_OK boxes=4 samples_per_box=524288 exact_inverse=4 wedge_angles=4` after independently evaluating four area-uniform cuboid point-pair distributions and four squared-distance moments. Cases were side triples \((1,1,1)\), \((1,1.7,2.4)\), \((0.8,1.2,2.7)\), \((1,2,3)\), with test radius \(0.64\) times the shortest side. The largest absolute observed difference between sampled and analytical CDFs was approximately \(1.41\times10^{-4}\), and the largest second-moment difference approximately \(1.13\times10^{-4}\).

The checker also compares four independently integrated rational wedge kernels with \((\pi-\theta)/\sin\theta\) and verifies the elementary-symmetric inverse on all cases. The exact face and wedge integrals, vertex error bounds, and algebraic inversion are proved in `RESULT.md`; finite numerical experiments are only corroboration. SciPy's scrambled Sobol generator is pseudorandom and this output is not an exhaustive certificate of a general theorem or of novelty.
