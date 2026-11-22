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

The proof rests on an exact pair of overlap coefficients, a unitary Fourier–Floquet reduction, a two-dimensional projection-commutator calculation, and a Gaussian Laplace asymptotic. The supplementary checker establishes 135 cyclic spectral comparisons, 276 sharp phase-norm comparisons, and twelve moment-asymptotic comparisons; these are finite tests, not an infinite-dimensional certificate. Numerical sampling alone does not verify the Fredholm essential spectrum, the absence of eigenvalues, or the all-iteration asymptotic; each of those conclusions is supported by the analytic proof in `RESULT.md`.

Execute `python verification/check_staggered.py` in an environment with the listed NumPy requirement. Scientific limitations, including historical-priority uncertainty and restrictions to the bilateral equal-width geometry, are stated in `RESULT.md`. Independent audit has not been performed.
