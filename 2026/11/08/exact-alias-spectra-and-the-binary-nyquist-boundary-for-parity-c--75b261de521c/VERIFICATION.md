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

Run with Python 3 and NumPy (see `requirements.txt`). The reproducible `check.py` enumerates finite abelian characters, constructs the normalized Fourier restriction matrix on the checksum-zero observation set, and computes its Gram eigenvalues. It also enumerates diagonal character cosets and checks the occupancy multiplicities, upper spectral endpoint, and first aliasing census. A completed replay checked 69 cases with maximum numerical eigenvalue residual approximately \(1.03\times10^{-14}\). Direct finite diagonalization is corroborating evidence, not an exhaustive proof for arbitrary group orders and lengths. Exact symbolic steps are stated in `RESULT.md` and use only character orthogonality and multinomial enumeration. No independent audit has been performed.
