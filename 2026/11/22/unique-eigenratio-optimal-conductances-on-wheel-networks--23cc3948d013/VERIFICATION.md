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

# Reproducibility and verification boundaries

Use Python 3 with NumPy and SymPy available and execute `python verify_wheel_eigenratio.py` from this directory. The script is standalone, builds each wheel Laplacian directly from independent edge conductances, computes eigenvalues, evaluates the exact proposed formula, and compares it against randomized nonsymmetric and off-optimum symmetric allocations. It additionally verifies symbolic characteristic-polynomial factorizations for four sizes.

The expected first output line is `VERIFY_OK 3910 spectral, minimax, nonsymmetric, exact polynomial comparisons`. The following size-specific lines report rim rate, minimal ratio, rim budget fraction and the relative gap. All random generators are explicitly seeded.

The mathematical proof is in `RESULT.md`: (1)--(3) establish unrestricted upper and lower spectral bounds; (4)--(7) give a sharp scalar minimax solution; (8) checks attainment through a complete Fourier spectrum; and (9) proves rigidity of all equality cases. Analytic Taylor series then prove the infinite-size comparison. These steps do not rely on finite numerical tests. Floating eigenvalue checks have tolerance and cannot certify global originality, all real parameters, or mathematical independence.

The literature comparison distinguishes a prior exact spectral-gap wheel theorem and a prior exact discrete-time fastest-mixing wheel theorem from the eigenratio allocation, and acknowledges that generic eigenratio weight optimization is previously established. Independent audit has not been performed.
