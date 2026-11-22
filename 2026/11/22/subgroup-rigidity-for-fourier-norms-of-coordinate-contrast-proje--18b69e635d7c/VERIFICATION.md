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

The analytical certificate is the proof in `RESULT.md`. The exact normalization uses the unitary Fourier transform on the finite product group: the two-dimensional transform of the kernel differs only by a frequency-column permutation from the Fourier-conjugate orthogonal projection. Its Fourier \(\ell^1\) norm is therefore exactly the entrywise norm used in the proof.

Run `python check.py` with NumPy installed. It tests all subsets at the specified small cyclic and product-group orders, the sharp norm and coset condition, and independently compares the direct two-dimensional FFT on three labelings. Output from the recorded run: `PASS: 3910 exhaustive subset cases, abelian product examples, and normalization checks`.

The finite checks do not prove the universal theorem, certify novelty, or replace the analytic argument. No independent mathematical audit was performed. The precise nondivisible minimum and quantitative stability remain unproved.
