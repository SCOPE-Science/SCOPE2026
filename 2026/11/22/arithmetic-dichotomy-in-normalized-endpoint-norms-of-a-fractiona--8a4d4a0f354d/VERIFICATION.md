---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The frozen display defined u=Re(K⁻¹) but used undefined ν in the theorem and proof. The complete corrected RESULT.md in repairs/3 defines ν=Re(K⁻¹) and uses it consistently; the original checker uses u for the same quantity. Rechecking the corrected claim: differentiation gives only the two maxima ±θ, common positive drift v and conjugate curvatures K and its conjugate. The exact ℓ² boundary maximum is e^{ct}, whereas the ℓ¹ norm is the coefficient absolute sum. A real Gaussian majorant near each saddle gives a uniform window asymptotic with the corrected Gaussian width; the complex Gaussian integral gives the claimed chirp sign and the factor 2. The centered derivative vanishes at both saddles and is bounded even at the branch point for α>1. Its Parseval bound and weighted Cauchy–Schwarz yield an O(L⁻¹ᐟ²) normalized tail outside L√t. The nonzero angular harmonics disappear by bounded geometric sums and Abel summation in the irrational case. For a/q, residue Riemann sums are uniform in the periodic phase and select the harmonics at multiples of q; the first has nonzero Gaussian integral sqrt(2π/(ν+2iqω)), so π/q is fundamental. The constant term yields the stated mean and real times give both extrema repeatedly. These checks are replayable in the repaired proof; the frozen verification notes and CHECK.py were inspected, not executed. The FFT diagnostic is not a proof of the tails or a uniform-in-α rate.

## originality

PASS

After the notation repair the surviving claim is the same fixed-order rational/irrational law with exact continuous-time normalization and periodic profile. It is distinct from the general fractional-shift framework and the earlier finding that multiple-maxima interference can sometimes obstruct convergence. No distinct exact or stronger coverage was established in the inspected sources.

## value

PASS

The repaired result computes the endpoint-to-Hilbert norm ratio for a canonical fractional-shift family in a genuine same-velocity interference regime. It resolves both exact convergence and the complete periodic obstruction, quantifying limiting extrema rather than just finding two subsequences with different values. This is a concrete nonadditive benchmark not supplied by the general separated-maxima theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
