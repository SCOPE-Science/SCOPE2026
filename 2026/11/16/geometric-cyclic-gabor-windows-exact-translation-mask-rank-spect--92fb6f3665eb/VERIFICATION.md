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

# Reproduction and boundaries

With Python 3 and NumPy, run `python check_geometric_masks.py` after extracting the two files to the same directory. The program directly constructs the finite cyclic Gabor synthesis matrix and compares its rank with the arithmetic formula, including singular masks; for valid masks it independently checks the complete eigenvalue multiset, the sharp endpoint constants and the product determinant. It tests the uniqueness and the even-modulation-index radical of the global taper minimizer.

Observed output: `CHECK_OK masks=506 full_spectra=36 optimizer_pairs=42`.

These finite computations are not a proof for arbitrary dimensions, and numerical rank tolerances cannot certify a singularity. The all-order exact proof is the fiber factorization and Fourier evaluation in RESULT.md; the nonstandard mask-rigidity argument is the circular binary-transition step. The uniqueness proof is analytic, not based on a finite root search. The source publication date is the first arXiv submission, not the later revised version. External mathematical validation remains unperformed.
