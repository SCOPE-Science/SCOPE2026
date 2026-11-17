---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

The local current-balance telescoping identity proves uniform measure on each fixed-occupancy sector and hence Bernoulli product stationarity. The exact signed total current is Fq=u(1-u)(1+qv)+v(1-v)(1+qu), with any real q implemented by strictly positive forward/backward rates. Setting s=(u+v)/2,d=(u-v)/2 gives F=2s(1-s)(1+qs)+2[q(s-1)-1]d²; no nonzero-d interior maximizer exists by indefinite Hessian, and boundary maxima are 1/4 at half-filled single lane for q<0. The diagonal has unique maximizer xq and value S(q), crosses 1/4 exactly at qstar=-1.3570032053..., the unique root of 32q³+85q²+80q+32 in (-1.5,-1). Independently verified change-of-variables, resultant polynomial, and root using exact symbolic algebra. No dynamic density selection claimed.

## originality

PASS

Best-of-knowledge: core original contribution is not established as a corollary or stronger prior result by the materially inspected sources and searches. The stationary polynomial from Popkov makes the new optimization calculable but does not itself assert the complete global-maximizer set or first-order-like external allocation jump. Three-lane fixed-total constraints do not reduce to the independently free two-lane problem. Residual priority risks remain; a failed search is not an originality proof.

## value

PASS

An exact phase boundary and complete optimizer classification for a physically realizable bidirectional exclusion process provide a nontrivial design trade-off between distributed and single-lane signed transport. The rate positivity extension unlocks a coupling range inaccessible to forward-only models.

The dated certificate retains the supplied scientific assessment, sources and limitations.
