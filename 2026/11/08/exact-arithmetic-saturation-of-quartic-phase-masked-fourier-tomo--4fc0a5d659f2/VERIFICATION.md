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
The exact rank proof uses Fourier orthogonality, a finite-field character sum, multiplicity counting and nonzero Vandermonde minors. Numerical checks are corroboration, not a proof for all primes.

Run `python CHECK.py` with the NumPy version declared in `requirements.txt`. It verifies the cubic image profile over many primes; compares directly assembled real Hermitian measurement matrices with the formula for small primes; checks traceless diagonal and within-fiber kernel witnesses; and tests unsaturated Lagrange interpolation null vectors. The checker's last line reports the actual number of passing assertions. Independent auditing remains unperformed.
