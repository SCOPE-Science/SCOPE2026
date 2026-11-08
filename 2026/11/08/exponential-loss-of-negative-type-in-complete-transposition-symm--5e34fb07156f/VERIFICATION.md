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

The standalone `verify_roundness.py` reconstructs character tables by the Murnaghan--Nakayama rim-hook rule, verifies integer class sums and column orthogonality, and checks the sharp \(S_3,S_4,S_5\) Fourier formulas. The \(S_5\) sign crossing is bracketed by exact rational integer-root bounds at \(3/10\) and \(8/25\); the derivative bound uses rational inequalities. A separate dense numerical diagonalization of the \(S_5\) metric matrix is performed when NumPy is available, and it confirms one zero nonconstant Fourier direction and 118 strictly positive directions for the centered Gram form.

Actual checker completion marker: `ALL_CAYLEY_ROUNDNESS_CERTIFICATES_OK`.

The general \(n\)-dependent exponential obstruction is proved analytically using the Jucys--Murphy content product and a fractional-power Laplace integral; finite tests do not prove it. No independent mathematical audit or external validation has been performed.
