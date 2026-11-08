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

# Reproducibility and scope

Run `python CHECK.py` with `numpy` installed, using the dependency in `requirements.txt`. The test constructs each complex projector explicitly and compares nonzero singular values of the full lifted matrix with the residue-count prediction, including even and odd orders. Exhaustive subset checks through dimension 10 verify the maximum-rank inequality and canonical optimizer; small even dimensions additionally check every parity-saturation optimizer count. Direct augmented projector tests verify the rank increment from coordinate measurements, and a separate Hermitian orthonormal-basis construction checks the equality of complex and real singular-value normalization. In the checked environment the output was `QUADRATIC_CHIRP_PROJECTOR_SPECTRUM_CHECKS_PASSED 11651`.

These finite tests corroborate the formulas but do not prove them for unbounded cyclic orders. The universal proof is supplied in `RESULT.md`, based on a unitary Fourier transform in the modulation index, geometric-series orthogonality, Euler-totient counting, and exact occupancy inequalities. Numerical singular comparisons use an absolute error tolerance of \(2\cdot10^{-10}\). No independent mathematical audit or external validation has been performed.
