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

# Reproducibility and verification

The exact mathematical proof appears in RESULT.md. The proof is direct. Its critical step is a uniform lower bound on the Gram matrix of normalized coherent kernels along generic complex rays: distinct unitary linear parts separate at infinity, while equal parts with distinct translations give a fixed strictly positive definite coherent-state block. All steps, including Liouville weight identification, compact perturbations, and sharp cyclic chirps, are detailed explicitly.

Run `python3 checker.py` using Python 3's standard library. Its deterministic output for the packaged source is:

`WEYL_FOCK_AFFINE_FINITE_DIAGNOSTIC_OK 9448`

The diagnostic checks finite Fourier chirp autocorrelations and constant Fourier magnitudes for sizes \(2\le N\le90\), plus coherent-kernel normalization and exact cross-phases for explicit noncommuting two-dimensional unitary matrices and translations. Its finite checks do not establish statements for all dimensions, all symbols, or infinite sequences. Those quantifiers are handled by the proof, which is not independently validated.

Scientific limits: the theorem assumes unitary affine linear parts, finite sums, arbitrary nonzero entire weights and the standard complex Gaussian Hilbert Fock space. It claims a sharp universal **lower** essential-norm bound, not an exact essential norm for every individual finite sum. It does not require the later-published one-variable finite-sum rigidity theorem as a proof input.
