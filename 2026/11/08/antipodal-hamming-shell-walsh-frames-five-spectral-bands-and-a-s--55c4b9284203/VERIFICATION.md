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

Run `python3 artifacts/verify.py` with Python 3 and NumPy. On the exact enclosed program the observed output is `ANTIPODAL_TWO_SHELL_CHECKS_PASS 3566`.

The program builds all Walsh characters through degree two as a real matrix, evaluates them on every point in two complementary Hamming shells, and diagonalizes the normalized Gram matrix for all admissible offsets in dimensions 5 through 11. It compares every eigenvalue with the five theoretical bands plus one zero, and checks the null rank and shell size normalization. It separately applies exact rational arithmetic to verify the five optimized eigenvalues, their extremal ratio and nearest admissible competitors in dimensions \(n=m^2\) for \(3\le m\le500\).

The proof in `RESULT.md` supplies the independent all-dimensional argument using moment identities, permutation-sector decomposition, adjacency multipliers and strict parity-separated bounds. Numeric eigenvalue comparisons cannot establish an infinite theorem; rational tests over finite ranges do not establish uniqueness for all dimensions. The full sampling operator has a one-dimensional kernel, so condition numbers refer to the quotient. No independent external validation or audit has occurred.
