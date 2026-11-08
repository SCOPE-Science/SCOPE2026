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

# Reproducible checks and their limits

From the package directory, install the dependency declared in `requirements.txt` and execute `python CHECK.py`. With `mpmath>=1.3.0` and 90 decimal digits, the current package reports `PASS: 717 high-precision finite-dimensional assertions`.

The checker compares two independently evaluated transition-amplitude expressions (generalized Laguerre and direct Fock coefficients); confirms the leakage/compression identity by summing the Fock monomial tail; reconstructs full Gram eigenvalues from two different matrices; verifies exact factorial minor identities; and checks the predicted constants at small separations for multiplicities one through five. The exact multiplicity-two eigenvalue formula is checked at multiple separations.

The infinite-dimensional, arbitrary-multiplicity conclusion is proved analytically in `RESULT.md`, especially the uniqueness of the leading exterior minor and its nonzero Vandermonde coefficient. Finite-precision numerical testing cannot establish all-parameter assertions or rule out publication overlap. The asymptotic estimate is for fixed multiplicity as the separation tends to zero.
