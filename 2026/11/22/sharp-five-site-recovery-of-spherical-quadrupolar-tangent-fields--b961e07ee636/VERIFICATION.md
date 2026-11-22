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

# Verification and reproducibility

The exact-degree Fourier decomposition, associated-Jacobi helicity zero factorization and global quintuple-band minimax inequalities are proved in `RESULT.md`. The result holds for all integer degrees at least one and all admissible heights, while the sharp optimal conditioning assertion is for degree two. The relevant normalizations and limits are made explicit in that proof.

Run `python CHECK.py` with Python, SciPy, NumPy and SymPy installed. The script independently constructs full complex tangent-component point-sampling matrices using associated Legendre evaluations and their three-term derivative recurrence; it tests every claimed degree-two singular value at eleven representative latitudes (including all singular heights), verifies symbolic polynomial and Jacobi identities through degree ten, and checks equatorial parity rank through degree eight. Successful output ends with `All direct Fourier-block, parity, rank, spectral and cubic checks passed.` Numerical tolerances are explicit in the checker. None of the finite checks substitutes for the analytic all-degree proof or a historical-priority assessment.

No external independent mathematical audit or validation has been performed. Reproducibility is conditional on the documented source spaces, sampling pattern and floating-point libraries; no claims about general vector-band recovery or arbitrary sensor configurations are certified.
