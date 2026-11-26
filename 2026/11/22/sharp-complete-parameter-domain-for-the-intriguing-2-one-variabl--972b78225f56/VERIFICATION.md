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

The claimed real parameter domain follows from the exact mixed density. With k=x^(-gamma) and w=x^alpha(1/y-1), logarithmic differentiation of the positive C_y gives x C_xy/C_y=1+alpha-gamma+gamma k log(1+w)-alpha(k+1)w/(1+w). Each x realizes all w>0, with w=0 a limit; k>1 ranges up to infinity when gamma>0. The grounded extension is continuous: C≤x handles x=0 and convergence at y=0 is locally uniform for x bounded away from zero. The correct uniform margins and mixed-density rectangle integration then give the copula criterion, including boundary rectangles by continuity. For gamma<0, w→infinity at fixed x violates it; for gamma=0, the infimum is 1-|alpha|. For gamma>0, alpha≤0 the infimum is 1+alpha-gamma at w→0. For 0<gamma<alpha, taking w=alpha/gamma-1 as k→infinity gives a strictly negative coefficient of k. In the remaining range let r=alpha/gamma≤1 and z=r(1+1/k). Where z>1 the minimizing w=z-1 subtracts gamma k(z-1-log z) from 1+alpha-gamma; otherwise there is no correction. The derivative of k(z-1-log z) is r(1-1/z)-log z<0 there, so k→1 gives the global infimum. This yields the linear branch when gamma≥2alpha and the logarithmic branch otherwise. For alpha≤1 these give alpha≤gamma≤1+alpha; for alpha>1 the logarithmic branch is strictly decreasing, its value at gamma=alpha is 1-alpha(1-log 2), and its value at gamma=1+alpha is strictly negative. This proves existence, uniqueness and the included terminal equality; negative boundary infima yield negative interior densities by a limit. Independent decimal bisection gives Gamma(2)=2.7979623075430878255155… and 1/(1-log 2)=3.2588913532709294545979…, agreeing with the displayed truncations. The uploaded checker was inspected but not executed and is not needed for the quantifiers.

## originality

PASS

The inspected same-formula source supplies sufficient subregions, not the exact arbitrary-real domain. The broader positive-exponent band, negative shapes and curved sharp boundary are supported distinct claims. Published priority is not certified.

## value

PASS

The exact admissibility region for an existing copula family resolves which parameters may be used without a negative rectangle mass. The nonobvious backward extension to negative shapes and the sharp curved cutoff above alpha=1 materially change that domain, beyond simply verifying the original sufficient box.

The dated certificate retains the supplied scientific assessment, sources and limitations.
