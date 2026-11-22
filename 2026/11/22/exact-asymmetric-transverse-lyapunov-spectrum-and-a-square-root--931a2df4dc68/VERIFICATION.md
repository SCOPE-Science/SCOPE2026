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

# Verification notes

The exact proof reduces the diagonal to logistic parameter four, diagonalizes all derivative matrices in a fixed Fourier basis, and evaluates the transverse average by an explicit Jensen factorization. The logarithm is integrable also when an individual transverse factor vanishes; the almost-everywhere statement excludes exceptional precritical orbits. The included `verify.py` independently recomputes the Jacobian, Fourier eigenvalues, complex-radical identity and numerical integrals. Execute with `python verify.py` from the extracted files; it uses Python 3, SymPy and mpmath and emits `VERIFY_OK` upon success. Computed quadratures are consistency checks, not proofs. No independent external mathematical validation is asserted.
