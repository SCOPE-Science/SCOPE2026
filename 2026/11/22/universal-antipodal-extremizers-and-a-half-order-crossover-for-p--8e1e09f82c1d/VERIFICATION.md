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

# Verification of the sharp Poisson-mixture approximation theorem

## Reproduction

Place the supplied standalone `check.py` in a directory with Python 3, SymPy and mpmath installed and run `python check.py`. On the reviewed package, it completed with `PASS: 32 exact-symbolic and numerical consistency assertions`.

## Actual checks

The independent algebraic route in `check.py` verifies the exact mixed-angle/log-radius curvature, the closed half-arc second derivative for one radius, the derivative identity for the odd dilogarithm, and the mean-projection boundary normalization. Bounded odd Fourier sums are checked against the dilogarithm closed form for five radii with an explicit safe truncation tolerance, and radial derivatives agree with the independently differentiated closed expression. For three nontrivial positive mixtures and four distinct angles, the strict mixed-difference sign is checked numerically. The four fixed-order fractional small-time coefficients are compared with independently computed truncated Fourier sums, and the Poisson sharp boundary slope is tested at three radii approaching the identity. These checks use symbolic identities where claimed and high-precision numerical tolerances otherwise.

## Scope and proof status

The full quantified theorem relies on the analytic Jordan-derivative arc representation, Parseval identity, convex logarithmic-radius phase, equality rigidity and rigorous harmonic/Riemann-sum limit arguments in RESULT.md. Finite Fourier truncations, floating-point tests and symbolic identity evaluations do **not** themselves establish the sharp inequality for all real BV functions, exact optimizer uniqueness, infinite summation identities or the small-time limits. The arbitrary-mixture assertion, its strictness and the critical fractional exponent are proved analytically in that text. External independent mathematical auditing and historical priority validation have not been performed.
