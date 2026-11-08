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

# Verification evidence and limits

The included `verify.py` is self-contained Python 3 code requiring only the standard library. Run `python3 verify.py` next to the source. Recorded output: `VERIFY_OK 11215 exact and numerical assertions`.

The checker tests both piecewise-integrated edge moments against independent algebraic formulas for nine rational interior thresholds. It enumerates every labelled finite simple graph through five vertices, constructs its edge-level covariance matrix by directly classifying ordered edge pairs, and checks equality to the signless-Laplacian polynomial using exact fractions. The same cases verify that the covariance nullspace dimension equals the number of bipartite connected components. Selected examples reconstruct the signless Laplacian by a numerically diagonalized principal square root, and three seeded direct vertex-label simulations compare empirical covariance to the exact formula. Tests include empty, disconnected, bipartite, and odd-cycle graphs.

General validity comes from the complete analytical proof in `RESULT.md`, not exhaustive finite testing. In particular, the program does not certify the infinite dimension-independent result, the global sample-complexity inequality, historical priority, or optimality of the bound. Those steps are argued directly with edge-pair conditioning, positive-semidefinite functional calculus and Hoeffding's inequality. Independent mathematical review has not been performed.
