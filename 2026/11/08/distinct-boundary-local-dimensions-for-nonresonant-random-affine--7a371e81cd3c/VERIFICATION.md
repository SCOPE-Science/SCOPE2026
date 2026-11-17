---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For sufficiently small endpoint radii, inverse images remain in the exact affine endpoint branches; stationarity then yields U(r)=pU(r/a)+qU(r/b) and V(r)=pV(r/b)+qV(r/a). Positive drift makes each convex characteristic function dip below one then cross exactly once at positive kappa. For s<kappa choose barrier C r^s with Phi(s)<1, for s>kappa barrier c r^s with Phi(s)>1; compact max/min principle on [0,R] controls endpoints and gives c r^t<=U(r)<=C r^s for s<kappa<t. Log divide (with negative log r) gives local dimension. Tonelli identity int x^-t dmu =1+t int_0^1 r^-t-1 U(r)dr yields finite for t<kappa, infinite for t>kappa. Difference Phi0-Phi1=(p-q)(a^-s-b^-s) proves root ordering. Critical t=kappa not claimed. Independent bisection for (a,b,p)=(1/3,8,.55) gives roots .28171392907808834 and .5524212948436695; only corroborative.

## originality

PASS

Barański–Śpiewak nonresonant stationary dimension paper treats global Hausdorff dimension and singularity, while their earlier AM paper gives existence/support and a nonquantitative endpoint power estimate. Neither inspected result supplies two separate exact endpoint Cramér roots plus the strict moment thresholds. Resultary comparable critical zero-drift and other random-map results have different models/regimes. General renewal/Cramér-Lundberg comparisons remain a real residual risk, acknowledged rather than assumed absent.

## value

PASS

Endpoint local dimension and inverse-distance moment integrability are natural invariants of singular full-support stationary measures, not arbitrary slices. Distinct roots explicitly reveal biased boundary concentration despite reflection-related map geometry; useful for boundary singularities and weighted observables, independent of computing global Hausdorff dimension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
