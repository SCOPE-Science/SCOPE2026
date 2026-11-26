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

On this same label stream, write G_r for the number of draws after reaching r distinct labels until reaching r+1. The independent spacings have success probability (m−r)/m. The event B_m>b is exactly that the first b draws are distinct; hence E[C_m|B_m>b]=b+mH_(m−b), including b=m. Expanding B_m as the sum of its tail indicators gives the negative double sum, with a strictly negative b=2 contribution even for m=2 (covariance −1/2). On B_m=b≤m the bth draw is a repeat and the future is an independent collection started with b−1 labels. Adjacent conditional laws therefore differ under the shared-spacings coupling by a geometric variable minus one, positive with positive probability, or by the final geometric variable for b=m versus m+1. The same conditional mean formula gives 1−x²/2 by summing r/(m−r) for r up to b−2 on the birthday scale. In the covariance sum, b/√m→x gives the Gaussian survival e^(−x²/2) and penalty x²/2. The b≤m/2 part is bounded on the scaled grid by a Gaussian times a quadratic, and b>m/2 contributes at most a polynomial-log factor times e^(−(m−2)/8). The resulting integral is sqrt(pi/8). The survival bound also justifies both Rayleigh moment limits for B_m, so Var(B_m)/m→(4−pi)/2; the independent geometric variances give Var(C_m)/m²→pi²/6 and the claimed correlation constant.

## originality

FAIL

The distinct indexed 2026/10/12 record already states the identical covariance, strict conditional order, conditional-mean limit and both asymptotic constants for the same stopping times, and supplies further conditional PGF and L² information. The mathematical claim is already covered regardless of unresolved priority in older published literature.

## value

PASS

As a theorem the joint comparison has substance: it explains why strict dependence persists for every size while correlation vanishes at a specified sharp rate, and identifies the scale at which conditional mean deviations remain visible. These are useful joint statistics of two standard stopping rules, beyond verifying their marginal formulas. The present record does not add to the exact earlier indexed result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
