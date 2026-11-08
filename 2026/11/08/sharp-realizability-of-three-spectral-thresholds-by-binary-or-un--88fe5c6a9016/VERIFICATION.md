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

# Reproducible checks

The standalone file `check.py` runs without third-party dependencies under Python 3. Execute `python3 check.py` in the same directory as this document. It produces `EXACT_SPHERICAL_TREE_CHECK_OK 46378` and exits successfully when the 46,378 finite rational assertions pass.

The checker corroborates finite mechanical-word telescoping, finite layer counts, explicit eigenvector recurrence coefficients, squared-norm identities, and concrete edited block discrepancies. It does not test the infinite sparse intervals at their literal astronomic indices, which are handled symbolically in the proof. In particular, finite tests do not verify the exact spectra, universal quantifiers over all slopes, or the infinite-dimensional surjectivity theorem. The written proof supplies the needed asymptotic and operator-theoretic arguments.

The spectral boundary exclusion uses a root discrepancy of order \(o(\log n)\), not merely an \(o(n)\) estimate. The approximate-point construction uses the adjoint's radial reducing subspace, not an assumption that the backward shift is diagonalizable. Independent mathematical audit has not been performed.
