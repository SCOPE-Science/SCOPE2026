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

# Verification of the spectral multiplicity theorem

The proof checks the inverse decomposition, positivity and exact rank of the operator coefficient, the mutual singularity and density kernels of the critical pieces, and the minimality/rank dictionary for the direct-integral Naimark representation. These mathematical arguments cover all stated Hilbert dimensions.

To reproduce the supplementary finite diagnostics, run `python CHECK.py` in an environment with Python 3, SymPy and NumPy. It reports `BILINEAR_DILATION_MATRIX_CHECKS_OK 588 exact inverse identities; 24 positive-rank density probes`. The exact checks cover four dimensions and three rational couplings. The density eigenvalue probes use floating-point arithmetic with stated margins. No finite enumeration proves the all-dimensional assertion.

Relevant source inspection includes the primary preprint's theorem, scalar kernel, Schur-complement proof, and explicit dilation question. The closest two-dimensional variation-jump publication was read in full for comparison. An equivalence hidden in older general POVM literature is not excluded by the searches; the principal mathematical claim is not independently audited.
