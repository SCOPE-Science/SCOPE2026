---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Fourier differentiation gives the STFT as -i times a nonzero phase times W=(A+B)cos(theta)+i(A-B)sin(theta), with theta=pi Delta t and A,B the shifted odd Gaussians. They cannot vanish together. The same-sign and opposite-sign regions therefore force t=T/2 and 0, respectively, modulo T. No zero lies at nu=+-d; on nu=0 the zero set has exactly the time spacing T, proving the fundamental period. The ratio artanh(u)/u strictly increases from 1 to infinity, while the exterior log ratio minus 4 pi d nu strictly decreases from infinity to minus infinity. This proves completeness and puts equality in the three-zero regime. The Jacobian at t=0 is -pi Delta (A-B)(A+B)' and at T/2 is -pi Delta (A+B)(A-B)'. Differentiating the modulus ratios at the roots gives the stated nonzero signs; the derivative of artanh(u)/u is strictly positive for u>0. The critical derivative of order three of A+B is 8 pi exp(-1/2), checked independently by symbolic differentiation. The imaginary time derivative is negative after identifying its imaginary component; the oriented coordinate change (t,nu)->(nu, Im W) has positive determinant there. In these coordinates the transverse real map has a positive cubic leading term, hence degree +1. Expanding artanh(u)/u gives u^2=3 epsilon+O(epsilon^2). The signed totals agree on both sides and at equality. Replay via the two scalar equations and local derivatives in RESULT.md lines 35–85. The finite numerical checker was read, not run; exact zeros/charges are specific to the stated real gap, tones, window and (t,nu) orientation.

## originality

FAIL

The frozen classification is mechanically recoverable from the earlier exact pure-tone Gaussian spectrogram extremum analysis of Meignen–Laurent–Oberlin (2022), especially Appendix A, not merely from an older qualitative ridge heuristic. Apply its two analyzed phase slices with A=1 and sigma=1. After removing the frequency-dependent time phase, minus the frequency derivative of the Gaussian-window transform divided by 2 pi is the first-Hermite reduced transform (up to constant gauge). At the constructive slice all Gaussian spectrogram extrema correspond to first-Hermite zeros. At the destructive slice the stationary central Gaussian zero is extraneous, leaving precisely the two noncentral extrema. The paper's exact derivative equation at the two slices gives the interior and exterior root equations directly, and differentiation and the first nonconstant Taylor term of the same scalar equations give the local indices, cubic contact and splitting. The later Resultary cusp theorem also explicitly specializes to the entire frozen geometry, but its later date is not evidence of prior coverage. The failure is based on the 2022 equations and results, not on failure to retrieve a different paper.

## value

FAIL

The phase map is a clear deterministic example, but its claimed precise zero census, critical separation and root positions are alternate descriptions of the old extremum calculation on the same tones. The orientation signs and local splitting are direct derivative and Taylor consequences in these coordinates; no scientifically distinct invariant or nonroutine remaining result was established for the narrow frozen claim. The later unequal-amplitude or higher-derivative classification is separate and not a repair of this finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
