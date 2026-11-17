---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

For stationary W_h=X/ell, the independent-Laplace product M_h(t)=product_{j>=0}(1-t^2 exp(-hj))^{-1} gives K_h=Li_2(t^2)/h-(1/2)log(1-t^2)+O(h), with two derivative controls on compact t subintervals. Positive curvature and Lambda prime tending to infinity define a unique saddle t_y. The tilted Laplace factors admit an integrable Fourier majorant from the first floor(1/h) factors, proving a uniform local density limit of order sqrt(h), not just an ordinary CLT. Tilting the half-line integral and applying the endpoint Euler-Maclaurin multiplier establishes the exact stated sqrt(h)/[t_y sqrt(2pi(1-t_y^2)Lambda''(t_y))] prefactor for each fixed y>0 uniformly on positive compact sets. Small-y and large-y expansions follow by series and saddle inversion; no joint endpoint uniformity. These analytic steps were read from the actual RESULT.md; stored 48 numerical checks are supporting diagnostics only.

## originality

FAIL

An independently published 2026-11-08 RESULT.md, read in full, gives the identical stationary sharp dilogarithmic tail and full boundary prefactor under a reparameterization. Set epsilon=h/2, t=ell theta, and prior threshold y_prior=ell*y/2. The prior cumulant Lambda_ell(theta)=Lambda(t)/2, prior I_ell(y_prior)=I(y)/2, and its prefactor sqrt(epsilon)/[theta sqrt(2pi Lambda_ell''(theta)(1-ell^2 theta^2))] exactly becomes the submitted sqrt(h) coefficient. Its exponent becomes I(y)/h. Therefore the whole submitted conclusion (including the supposedly distinguishing prefactor) is already covered. Relative same-day posting order is unknown, but extant scientific coverage is decisive for this review. Earlier Nov 2 papers cover only the rate, not the prefactor.

## value

FAIL

The sharp tail for an actual resetting process is a mathematically motivated observable, but this specific claim reproduces an already published full formula and supplies neither a new regime, independent invariant nor a substantive generalization. An alternative derivation and numerical checker do not establish a new valuable mathematical result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
