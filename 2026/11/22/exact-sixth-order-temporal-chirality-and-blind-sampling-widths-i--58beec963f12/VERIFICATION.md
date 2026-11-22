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
# Verification procedure and limits

The standalone `check.py` is embedded with the finding. Executing `python check.py` verifies the symbolic three-state Fourier coefficient, direct matrix exponentials of the original generator, independent three-dimensional Gauss–Legendre quadrature of the conditional-Gaussian three-time moment and exact null-width/degeneracy cases. The observed test result was `PASS: 66 symbolic and independent matrix/quadrature checks`.

The infinite family of positive blind widths and the all-parameter sign factorization are established analytically in `RESULT.md`, not extrapolated from finite tests. The script does not constitute an independent scientific audit; publication-priority uniqueness and finite-sample detectability have not been independently assessed.
