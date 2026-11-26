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

For the stipulated unit-penalty, plus-dual, simultaneous quadratic updates, differentiating one block gives (s+2)x_i^+=(s+1)x_i-S-lambda. On the zero-sum space this multiplies by b=(s+1)/(s+2); the independent sum/dual block has trace t=(2s+3-2m)/(s+2) and determinant q=(s+1-m)/(s+2). In the quadratic Schur test the only nonautomatic inequality is 1+t+q=(4s+6-3m)/(s+2)>0. At equality a real eigenmode alternates with multiplier -1 (including m=2, s=0); below, P(-1)<0 forces a real root below -1. Thus the strict threshold is necessary for all states and sufficient irrespective of Jordan blocks. For s<m-1 the roots straddle zero. The positive root is at most b by P(b)=ms/(s+2)^2; the negative root increases strictly, since (t'lambda_- - q')/(2lambda_- - t)>0. Its magnitude crosses the increasing b exactly once, from m-1 at s=0 to zero at m-1, with the crossing above the stability boundary. P(-b)=0 gives the claimed quadratic and positive root. For s>=m-1 complex roots have modulus sqrt(q)<b; if real, the roots are nonnegative and P(b)>0 with b>t/2 places both below b. Hence no other global minimizer exists. Expanding the positive root and b gives the stated 4/3 asymptotic gap ratio. This is a spectral radius, not a one-step norm bound.

## originality

PASS

The scheme itself is classical. The supported distinct claim is the exact all-m threshold and unique asymptotic spectral tuning for this one homogeneous fixed-penalty Jacobi benchmark, not a general ADMM theorem or a priority certification.

## value

PASS

This is a motivated sharp calibration of the established generic damping prescription on a natural test problem where every parallel block participates in the same constraint. The exact instability boundary and optimal coefficient distinguish stability from best rate, and identify competition between a positive disagreement mode and a negative coupled mode rather than a repeated-root optimum. The 4/3 leading spectral-gap gain quantifies a real difference from the general sufficient prescription on this benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
