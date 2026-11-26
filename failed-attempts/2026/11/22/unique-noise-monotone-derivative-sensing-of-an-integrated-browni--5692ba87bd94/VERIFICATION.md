---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Integrating the bridge kernel gives the piecewise cross-covariance for the derivative reading, prior trajectory risk 1/30, and area covariance t(1-t)/2. Squaring and integrating the cross-covariance gives the stated F, independently verified along with the derivative and high-noise gain ratio. The cubic f has one root in (2/5,5/12): it decreases to its only critical point in (0,1) and is negative from that minimum through 1. The noise coefficient changes sign at alpha; between beta and alpha both A and B_* increase strictly, while outside that interval their signs agree. Hence the derivative of the gain changes from positive to negative at exactly one interior time, with neither observation endpoint informative. Implicit differentiation gives positive noise sensitivity and simple-root Taylor expansions at zero and inverse noise zero. The terminal-area gain is strictly increasing in t(1-t), which is uniquely maximal at the midpoint; the high-noise path gain ratio is F(alpha)/F(1/2), not a ratio of posterior risks.

## originality

FAIL

Two distinct mirrored statements give exact coverage of the two constituent optimizations. The velocity-mode proof, not merely the threshold statement in its Finding, supplies the same root curve for every noise level and the exact gain. The beta-weighted one-point theorem supplies the midpoint and the exact area risk at n=1. The remaining endpoint Taylor coefficients, contrast and relative high-noise gain follow mechanically from the covered equations and locations. Neither source's date establishes chronological priority; the failure is mathematical coverage.

## value

PASS

The underlying classification makes a meaningful distinction between reconstructing a cumulative trajectory and estimating its terminal value with the same instrument. The systematic finite-noise displacement from the midpoint is more informative than claiming a large performance gain. As a narrow remainder after crediting the two existing designs, numerical evaluation of the relative gain and juxtaposition of the already classified locations do not support a distinct repaired finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
