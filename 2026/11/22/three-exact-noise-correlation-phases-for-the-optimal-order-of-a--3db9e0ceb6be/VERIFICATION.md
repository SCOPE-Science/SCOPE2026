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

Unrolling the update makes the bias (1-x)(1-2x)(1-4x)y0 common to all six orders; temporal zero means eliminate the cross term with this deterministic bias, with no need for Gaussianity or conditional unbiasedness. The chronological innovation coefficients all sum to one minus the common contraction, so the variance differences vanish at rho=1 and their quotients by 1-rho are affine in rho. I reconstructed these coefficients by propagating them step by step and recovered the two stated crossing thresholds. For the proposed winner on each interval, I tested the five other orders at both ends after division by 1-rho. Substitution x=u/[4(1+u)] gives nonnegative coefficients for the oriented numerator and denominator of each nonzero comparison, hence strict positivity for u>0, and x=1/4 was checked separately. This gives 26 strictly positive endpoint comparisons and exactly four zero comparisons (the two boundary pairs counted in both adjacent regions); thus there are precisely the two claimed double ties and no others for -1<rho<1. The same method gives five strict threshold inequalities. An independent exact replay confirms all four quoted variances, the two-step swap identity and the absence of a Gaussian assumption.

## originality

PASS

Pass the complete fixed-multiset phase diagram, not the broader observation that AR(1) noise reverses optimal stepsize order. The closest distinct same-day result treats essentially the same loss and covariance and finds initial and terminal reversals, but its global optimum over the step cube is not the optimum over the six points with the prescribed rates. Its signal-to-noise thresholds and examples do not imply the x-dependent switch positions, boundary ties or exclusion of the other orders. The independent-noise fixed-multiset theorem is genuinely applicable at rho=0, and provides no coverage of the other phases. The inspected primary work did not establish this constrained classification.

## value

PASS

The result pinpoints when the descending-order rule ceases to minimize terminal quadratic noise risk even with equal marginal variances and a fixed total contraction. The signed correlation regimes select two different departures from descending order, and the first horizon at which this is possible is shown by the two-step swap identity. Giving the full continuum boundary and unique-order/tie classification for a canonical factor-two ladder is more useful than isolated reversal examples or a freely tuned schedule when an implementation must use a prescribed set of rates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
