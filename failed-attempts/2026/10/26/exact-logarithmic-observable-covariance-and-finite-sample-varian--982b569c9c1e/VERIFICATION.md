---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Reconstructed the proof for invariant Lebesgue measure and the centered logarithm, whose lag-zero variance is 1. Branch substitution x=(j+t)/q gives the logarithm of the gamma product; integrating the alternating power series for log(1+t) against log t gives C_1=1−pi²/24. Strictly decreasing branch average and −log t have strictly positive covariance. The positive Stirling remainder and 0≤t≤1 give a uniform bound |R_q(t)|≤1/q, so integration gives the claimed q⁻² bound. The stationarity tail is 2 sum_{j≥1} j C_{N+j}; geometric sums give the stated correction and (8/9)4⁻ᴺ error, including N=1. The Q_K bound uses the unweighted geometric tail. In a fresh, separate 40-decimal replay, independent branch quadrature and the gamma expression agreed through q=16, direct finite-sum integration agreed for N=1 through 4, c and C_1 agreed with the stated approximations, and K=16 tail enclosures for the variance rate and intercept were compatible with their displayed decimals. Replay: /workspace/branches/14a9f726-44f0-44fc-8d54-2abce474e800/independent_check.py with small_check.txt and full_check.txt. Numerical quadrature was not interval-certified. The uploaded VERIFY.py was inspected, not executed; its preparation run is separate evidence.

## originality

FAIL

A distinct indexed work gives the exact same covariance in dilogarithmic form for all integer bases, more terms in its sharp lag expansion, and the exact signed finite-window tail identity. Its branch calculation turns directly into the frozen gamma representation by the standard gamma product, and its convergent expansion gives the frozen explicit uniform bounds by elementary estimates detailed below. This is present mathematical coverage. The overlapping record has a later catalogue date, so it is not evidence that the frozen work lacked priority when prepared. Defaveri–Smith's earlier paper, by contrast, does not give the exact doubling covariance or correction in the passages checked.

## value

FAIL

The sharp bias and usable error bounds are meaningful for this observable. As a separate exact finding against the checked catalogue, however, the alternative gamma notation and uniform bounds follow by the standard product and an elementary bound on the already available convergent series; the variance correction is then the same geometric tail. The record provides a self-contained alternate proof but no separate uncovered invariant or sharper regime relative to that result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
