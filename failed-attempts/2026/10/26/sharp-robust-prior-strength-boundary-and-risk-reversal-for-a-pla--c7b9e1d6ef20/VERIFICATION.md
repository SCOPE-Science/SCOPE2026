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

On the stated real invertible 2×2, finite-strength, one-Gaussian-probe domain, diagonalizing the covariance gives an axis projector moment α/(α+β) for axis standard deviations α,β, by the elementary angular integral; the off-diagonal moment vanishes by symmetry. The trace of the complementary projector against AAᵀ then gives the claimed squared Frobenius risk. I reconstructed the baseline-gap factor, derivative quadratic and discriminant, and the exact (3,1,2/5) witness including the crossing at 7/3. The derivative sign at and between c1 and 1/2 follows from the leading, linear and constant signs and the value at r=1. The worst alignment is c0 by denominator monotonicity for r>1. With k=a²c0+b²(1−c0), writing the risk divided by ab in s=r−1 gives a weighted average of the coefficient ratios 1, (a+b)²/[2(k+ab)] and ab/k. The middle ratio is strictly above the smaller endpoint ratio, and both the constant and linear coefficients matter at finite s>0. This gives the stated minimax value and strict finite-attainment rules including k=ab. Replay exact checks with python /workspace/branches/math_checks.py 2; the frozen verifier and recorded angular diagnostics were inspected, not rerun. The mathematical result is not rejected for a proof error.

## originality

FAIL

There is exact equivalent catalogue coverage of the risk law, the certified-alignment minimax switch, its finite-attainment behavior and the strength-profile mechanism. For B=AᵀA and g=ω, samplewise the range-finder squared Frobenius loss is tr(B)−gᵀB²g/(gᵀBg), exactly the residual trace for one-column Nyström on B. Every planar positive-definite B is of this form. Use B eigenvalues a²,b², covariance condition number r² and c=cos²θ. The Nyström Finding equations (1)–(5) and proof §4 then give the laws at issue, not merely an estimate. The finite crossover and exact maximizing-strength expression not printed there follow by factoring the same quadratic risk difference and solving the same derivative quadratic. The exact risk also follows mechanically from the earlier bivariate spatial-sign covariance moment. The exact matching catalogue item has a later path date; the decision credits demonstrable equivalent coverage in the audited corpus and does not assert that that item was historically first or that the frozen record copied it.

## value

FAIL

The underlying decision problem is natural, and the threshold and reversal are useful. As a distinct finding here, however, the reported sharp curve and robustness conclusion are the same mathematical design problem under a samplewise loss identity. The remaining explicit crossing, derivative root and numeric witness are routine evaluations of that already complete curve, with no distinct access-model theorem, setting, or structural conclusion. A change from trace loss notation to squared Frobenius notation does not supply an independent scientific gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
