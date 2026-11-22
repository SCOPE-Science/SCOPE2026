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

`check.py` uses exact symbolic arithmetic to reconstruct the Fourier-moment Toeplitz matrix, reduces the critical determinant by the defining quadratic relation, verifies strict Bernstein-polynomial sign identities, and checks the small-width expansion. It then independently evaluates 31 admissible widths and 101 placements per width, directly diagonalizing the observation Gram matrices; the reported check count is 3140. Reproduce with `python check.py` with `sympy` and `numpy` available.

The full theorem holds for continuously many widths and placements because of the exact proof in `RESULT.md`; sampled matrices alone do not establish it. No external independent mathematical audit has been completed.
