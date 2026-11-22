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

# Verification and reproducibility

The proof is self-contained in `RESULT.md`. Its nonstandard assertions are the exact positive diagonal slack identity, the cosine-mode two-by-two block for alternating edge probabilities, and the centered partial-sum bound. All are derived analytically for every integer \(n\ge3\); in particular, no finite search is taken to certify the universal inequality.

Run `python verify_path_stability.py` with NumPy installed. It generates feasible stochastic path matrices of sizes 3 through 20, plus a two-vertex boundary consistency case, and verifies 4,899 matrices. It checks row sums, spectral norms, cosine-vector normalization and eigenvector relation, the nonnegative slack identity, the squared-SLEM bound, exact equality on the alternating family, and each edge-bound normalization. Testing uses a fixed seed and approximate floating-point tolerances. Random tests cannot rule out counterexamples outside the sample or certify transcendental trigonometric identities.

Scientific scope: symmetric nonnegative stochastic tridiagonal matrices with uniform equilibrium and exact Euclidean SLEM. The equality and sharpness statements use the explicitly diagonalized alternating family. Independent audit has not been performed.
