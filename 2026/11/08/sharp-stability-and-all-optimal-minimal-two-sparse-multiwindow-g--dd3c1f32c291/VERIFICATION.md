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
# Verification and replay

The symbolic argument in `RESULT.md` is the unrestricted proof. Its critical Weyl-orbit frame eigenvalues, support-difference lag restriction, and exact zero-lag geometric sums are stated explicitly there. The non-antipodal lag eigenvalues are all \(Np(1-p)\), forcing the bound \(N/4\); antipodal lag eigenvalues split by modulation parity and give the sharp extra phase criterion. This establishes the exact optimizer classification for all \(N\ge3\).

To corroborate calculations with directly constructed projectors rather than replaying the same Fourier-sum code, use Python 3 with NumPy: `OPENBLAS_NUM_THREADS=1 python verify_sparse_optimal.py`. The program builds a Hilbert--Schmidt-orthonormal *real Hermitian* matrix basis, forms the full projector measurement matrix, computes its Gram spectrum, and compares the whole multiset with the claimed formulas. Actual execution completed with `CHECKS_PASS: direct_operator_frame_spectra 32 dimensions [3, 4, 5, 6, 7, 8, 9, 10]`. There are balanced, unbalanced, feasible-boundary and phase-sensitive cases.

This exact object-level numerical check does not establish the all-dimensional proof, independence of earlier research, generic noise performance, or priority. Independent audit is not performed.
