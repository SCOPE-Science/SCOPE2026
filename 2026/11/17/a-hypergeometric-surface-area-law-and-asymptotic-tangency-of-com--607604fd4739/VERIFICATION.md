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

# Verification

The proof in `RESULT.md` is analytic and all-dimensional. `checker.py` is a standalone numerical/finite geometric cross-check: it reconstructs all root vertices in the actual Euclidean zero-sum space, computes all facet volumes by Qhull in their affine spans for orders 3 through 6, and compares full-polytope volumes to an independent convex-hull computation. It checks the area hypergeometric tilt and a rigorous total-variation bound at eight orders. The command is `python checker.py` with NumPy/SciPy; expected last line is `ROOT_SURFACE_PASS`.

Exact finite experiments cannot prove a universal claim. The proof of hypergeometric convergence uses Stirling's formula, and the asymptotic remainder uses an analytic fourth-moment bound. No independent mathematical audit has been performed.
