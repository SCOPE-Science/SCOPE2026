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

# Verification of the mathematical package

`python check_mobius.py` compares the finite covariance formula against direct Moore–Penrose transfer-current matrices for sizes 3 through 30 and against independently enumerated uniform spanning trees for sizes 3 through 6. These enumerations contain 81, 392, 1815 and 8112 trees. Larger sizes 80, 160, 320, 640 and 1280 test convergence toward the predicted constant. All checks passed. `python symbolic_certificate.py` verifies the limiting Fourier-symbol determinant relation and endpoint identities exactly over radicals; it also passed.

The proof of the infinite-dimensional-in-size statement resides in `RESULT.md`: geometric antiperiodic Green kernel, full Fourier block diagonalization, connected cycle-matroid rank, uniform exponentially accurate limiting symbol and rank-one perturbation. Numerical tests are evidence of consistency but not exhaustive infinite proofs. Historical priority remains provisional; independent audit not performed.
