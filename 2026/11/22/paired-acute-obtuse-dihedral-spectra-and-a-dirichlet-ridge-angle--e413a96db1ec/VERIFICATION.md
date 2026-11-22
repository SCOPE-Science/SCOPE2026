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
# Reproducibility and limits

Run `python verify_loday_angles.py` in a Python 3 environment with NumPy. The checker enumerates every planar binary tree, constructs its Loday-coordinate vertex, independently determines all facets' tight vertex sets and pairwise affine ranks, and validates the exact squared normal-cosine sets and multiplicities for each integer \(n\) from \(3\) through \(8\).

Observed output includes `LODAY_RIDGE_ANGLE_PASS`, with \(5,14,42,132,429,1430\) vertices in consecutive cases and acute counts \(1,5,15,35,70,126\) and obtuse counts \(4,16,41,85,155,259\). The infinite-family claim is established by the algebraic and combinatorial proof in `RESULT.md`. The Dirichlet weak limit follows from uniform boundary-order-statistic spacings and a negligible set of nested boundary coincidences; the checker does not attempt to certify infinite-dimensional convergence. The exact count of right-angle ridges is zero.

Validation is a self-review, not independent external review, peer review, or formal proof certification. The source-priority comparison remains provisional.
