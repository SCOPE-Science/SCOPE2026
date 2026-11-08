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

Run `python3 verify.py` with NumPy. The supplied script independently computes two-site Fourier compression matrices for each absolute-frequency energy sector; compares their spectra with closed trigonometric eigenvalue products; searches all sectors for the strict minimum; and diagonalizes the actual dissipative adjacency Hamiltonian for three small prime-pair examples at shrinking loss. Checks include distinct energies at each sector, strict positivity, and numerical first-order convergence.

Verified pairs: `(5,7)`, `(5,11)`, `(7,11)`. Tensor-only check: `(5,7,11)`. For `(5,7)`, analytic rate `0.0021615158009654`; the measured rate divided by loss at `0.08`, `0.04`, `0.02` is respectively `0.00216094275167`, `0.00216137251045`, `0.00216147997658`.

These checks do not prove the arbitrary-prime theorem or give uniform error bounds in system size. The infinite-family proof is in `RESULT.md`.
