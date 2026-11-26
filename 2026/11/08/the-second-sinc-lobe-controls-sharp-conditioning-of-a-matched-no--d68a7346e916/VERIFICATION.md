---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Fourier transformation of the stated centered difference energy gives 2δ⁻²(1−sinc t); the two terms of the fixed inverse preconditioner then give the stated F, with both endpoint limits 1. I checked F'=N/t⁴ and the derivatives of N. The sign of N'' and the endpoint signs isolate a unique peak on (π,3π/2) and a unique second-lobe valley on (4π,9π/2); the remaining half-lobes have the stated derivative signs. As an independent early maximum bound, with x=t²≤10, the alternating expansion gives F≤1+7x/60−x²/140+66x³/362880. The upper polynomial is increasing on [0,10] and is below 1.64 there. For the first positive lobe after zero, N is convex and negative at both endpoints on [2π,5π/2], and N'>0 on [5π/2,3π] since the coefficients multiplying |cos t| and sin t are each greater than 12. Its unique minimum thus admits interval bisection. Independent outward interval bisection and evaluation over the root brackets gave the peak 1.644258263597434…, first valley 0.957508233089985…, second valley 0.957152026310063…, and ratio 1.717865311257030…. The lower Taylor bound for F near zero, the negative-sine lobes, and the increasing lower tail envelope exclude all other minima; the upper envelope excludes maxima after 2π. The constants are sharp because one may localize Fourier support arbitrarily close to the positive extremizing frequencies.

## originality

PASS

The general nonlocal symbol and Poisson-plus-mass framework are prior work. The supported distinct result is the sharp extremum pair and in particular the exact lobe selection for the matched box multiplier. No inspected known bound or exact result settles those quantities.

## value

PASS

The uniform box kernel is a standard test case and the calibration is set by the two frequency regimes, not tuned to manufacture an extremum. The result gives a sharp benchmark and corrects the plausible expectation that the first positive-sine lobe after zero controls the low spectral edge. The lobe ordering is an independently useful feature beyond the decimal condition number.

The dated certificate retains the supplied scientific assessment, sources and limitations.
