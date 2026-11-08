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

# Reproducibility and mathematical limits

The exact finite formulas arise from a normalized convolution kernel, not from approximate floating-point projection matrices. Run `python checker.py` in an environment with Python 3, SciPy and mpmath. The checker independently enumerates the \(3^d\) or \(4^d\) full kernels for each \(1\le d\le6\), tests all 12 exact rational identities, evaluates 12 large-d binomial expressions at 75-digit precision, and independently evaluates four rescaled Bessel integrals. A successful execution prints `ALL_FIRST_SHELL_PROJECTION_DIAGNOSTICS_PASSED`.

These finite checks cannot prove the uniform shifted-Stirling remainders or the asymptotic expansion of the Bessel integral. Those steps are analytically justified in `RESULT.md`: the log-gamma formula is uniform over three fixed residue cases, while the Bessel integral is split into a Gaussian dominated range and exponentially negligible tails. The continuous quadrature is intentionally diagnostic rather than a certified interval enclosure. The all-dimension sharpness is established by Fourier character orthogonality, kernel duality and invariant-projection averaging, not by enumeration.

The proof does not provide explicit thresholds beyond which the signed comparisons hold. No independent audit has yet been performed.
