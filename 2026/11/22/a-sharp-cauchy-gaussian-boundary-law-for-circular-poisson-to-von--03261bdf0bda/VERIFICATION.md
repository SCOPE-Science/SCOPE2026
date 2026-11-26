---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

With normalized Haar measure, positivity of the Fourier weights at all harmonics and strictness at the first give the unique alignment for κ>0. At κ=0 the error derivative in the aligned direction is -2r; coercivity follows from the squared von Mises norm growing as sqrt(πκ), with the cross term bounded at fixed r. For δ=1-r, scaling θ=δy gives limiting profiles 2/(1+y²) and sqrt(2πc) exp(-cy²/2) when δ²κ→c>0. Bounds by a Cauchy profile and a Gaussian on each compact positive c interval give L² convergence with measure dy/(2π), and the squared-norm and cross-integral constants give the stated F. Integration by parts in the Laplace representation of e^{x²}erfc(x) gives (xe^{x²}erfc(x))' as the positive decreasing integral in the proof, from 1 to 0, so F has a single interior minimum below its c=0 limit 1; F is strictly positive there because the profiles have different tails. The scaled error tends to 1 if δ²κ→0 by Cauchy–Schwarz and the Bessel norm, and diverges if δ²κ→∞ since the scaled cross term is at most 1+r. Comparison to the interior trial value forces tightness and then convergence for every sequence of global minimizers, without finite-r concentration uniqueness. The Bessel-ratio expansion gives the moment scale (2δ)^{-1}, placing it in the c=0 regime. Independent quadrature and bisection of the positive Laplace integral gave x≈0.5087827346880, c≈0.5177197422333, F≈0.0705689390523 and ratio ≈14.1705403741. Read VERIFICATION.md and verify.py as evidence; the bundled checker was not executed.

## originality

PASS

The closest exact circular L² comparison fixes a heat target and changes the Poisson scale, not the reverse. Their limit profiles are of the same types, but fixing the other width multiplies the scale-ratio objective by a nonconstant factor and changes the optimizer. No inspected statement transfers its optimum or the fixed-Poisson moment penalty to this setting. This conclusion is limited to the investigated sources.

## value

PASS

This is a concrete calibration problem for two commonly used positive circular kernels. The exact wrong-scale effect of first-moment matching is not apparent from visual concentration or pointwise approximations: the moment concentration grows at order δ^{-1} instead of δ^{-2}, and its squared loss is asymptotically about 14.17 times optimal. Uniform control of all global optimizer sequences and sharp, normalized coefficients make the theorem useful beyond a profile fit at a few radii.

The dated certificate retains the supplied scientific assessment, sources and limitations.
