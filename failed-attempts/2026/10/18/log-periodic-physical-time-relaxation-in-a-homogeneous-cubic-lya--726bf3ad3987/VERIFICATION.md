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

The dot and cross products with (x,y) give r'=r^3(-a+b cos 2theta) and theta'=r^2. Thus r^2=C exp(-2a theta+b sin 2theta). Independently integrating the inverse angular speed from minus infinity gives I'(theta)=exp(2a theta-b sin 2theta)>0; I is comparable to exp(2a theta) and is onto (0,infinity). The full forward orbit has I(theta)=C(t+D) with D=I(theta0)/C>0, and (t+D)r^2=I/I'=F evaluated at theta(t). The half-turn shifts log I by 2 pi a, so the angular quotient defines a positive smooth periodic function of log I. Replacing t+D by t perturbs the phase and factor by O(t^-1), by boundedness of the profile and its derivative. F'=1+(2b cos 2theta-2a)F rules out a constant when b is nonzero; b=0 gives 1/(2a). Monotone advance in log t gives every value in the continuous image of a period as an accumulation point, and ordinary periodic Cesaro averaging after u=log t gives the stated occupation law for bounded continuous tests. The polar solution exists globally and r(t)<=r0 exp(|b|), giving stability even for orbits with transient radial growth. The package checker was inspected, not executed; its finite quadratures are not the proof.

## originality

FAIL

A distinct published catalog record already covers the exact shifted-clock amplitude on the identical a>0 family and derives the nondegenerate accumulation interval. Its exact identity also directly implies the bounded-continuous logarithmic occupation law by Cesaro averaging, so that law is not an independent remainder. This is a finding of existing mathematical coverage, not evidence that the other record has historical priority: its catalog date is later than the frozen record's catalog date. Liu–Fitzsimmons are prior for the system, polar reduction and stability, not the inspected quantitative profile.

## value

PASS

The phenomenon is mathematically meaningful: global cubic stability and sharp order t^-1/2 do not force a constant radial prefactor. A reproducible exact clock and an initial-state-independent distribution on the surviving amplitudes quantify what the usual decay exponent misses. The value of the result as a description of dynamics does not remedy the documented overlap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
