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

# Verification details

The analytical steps to check are: compact irreducible Perron eigenvalue and spectral gap, the tail Green formula for each eigenvector coordinate, \(\sum_{j\ge1}|\lambda G_j-1|<\infty\), relative last-coordinate convergence for finite Perron eigenvectors, and the exact head/tail Schur complement. Each is proved in `RESULT.md` under explicit fixed positive parameters.

For independent numerical reproduction, execute `python CHECK.py` using Python 3 with `mpmath`, `numpy`, and `scipy`. It compares exact high-precision finite continuant roots with the predicted Green-product coefficient for several parameter choices. Finite numerical tests provide corroboration only, not proof for arbitrary \(N\). Source-priority limitations are described in `REVIEW.md`.
