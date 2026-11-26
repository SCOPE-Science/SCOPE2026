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

Reconstructed the killed four-state backward equations, using only the two incoming boundary conditions and scaling gap by L and time by L/v. The uniform absorption probability in bounded time is positive even when one rate vanishes, so the moment equations apply at both endpoints. With y=x/L and u=y(1−y), the sum of the moving-state means is 1+hu and their difference is 2y−1. For the dimensionless second moments, the difference is (2y−1)[1+1/r+(h/6)(1+2u)] and the sum is 1+1/r+h/6−(2−h−3h/r−h²/6)u+(h²/6)u². These obey both boundaries; the corresponding homogeneous problem reduces to (2+h)Δ=0 and is unique. Including the two stalled phases and integrating using ∫u=1/6 and ∫u²=1/30 yields the frozen first and raw second moments, variance and CV squared. The derivative of the latter has numerator 24r²[(r−4)h+10r+30], positive since 10r−4h≥8r over the full allowed interval. The other derivatives are positive termwise. This proves the endpoint minimizers, interior infima if endpoints are excluded, and unique balanced maximum. The supporting script was inspected, not run; its reported simulations are not the proof. No stochastic ordering is inferred.

## originality

PASS

The supported distinct result is the explicit first-contact moment pair and simultaneous strict ordering of the mean, variance and squared CV over individual rate splittings at fixed positive total, under the frozen initialization. The strongest inspected close results each fix the rates equal, vary a common rate for unequal speeds, or treat a stationary law of a different process. Known common-rate means and the backward-generator method are not credited as new. This is a best-of-knowledge claim comparison, not a publication-priority certificate.

## value

PASS

The first-contact allocation problem is natural, and minimizing variance need not minimize relative fluctuation after the mean changes. Here explicit moments and strict relative-risk monotonicity settle all three objectives at every dimensionless budget, with sharp endpoints even when a rate vanishes. This is useful beyond an equal-rate moment evaluation and does not claim a full-law ordering.

The dated certificate retains the supplied scientific assessment, sources and limitations.
