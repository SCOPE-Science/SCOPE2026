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

Normalized L² Gram for frequencies separated by y>0 is [[1,s],[s,1]] with s=sinc(y), hence the exact squared evaluation kernel is 2(1-s cos(xy))/(1-s²). For y>=2 the sinc bound is strictly below 1+3x²; for 0<y<2 the quadratic upper sine bound and polynomial F(u,z)=z²(20+10z-z²)/3600>0 establish strictness. A coalescing cosine/sine combination converges to 1+3xt, proving the optimal but unattained constant. Independently checked the exact rational polynomial identity and the normalization factor two; an analytic bound, not the source numerical loop, establishes universality.

## originality

FAIL

A published 2026-11-01 theorem for the identical two complex Fourier atoms and [-1,1] Lebesgue norm explicitly establishes sharp squared exterior constant (1+3x²)/2, the fixed-gap kernel K_y=(1-s cos(xy))/(1-s²), strict nonattainment, and the full quadratic collision defect. Multiplying by two for probability-normalized L² yields exactly this assignment’s main constant 1+3x². It also supplies an explicit maximizing representer, a strictly stronger coverage. This is exact numerical and mathematical identity, not an extrapolation from titles.

## value

FAIL

A sharp two-frequency bound is useful for extrapolation in isolation but it has already been published with the same domain, normalization after factor two, fixed-gap operator, strictness, and additional collision-defect information. Re-proving it by a different elementary sine bound is not a distinct valuable mathematical result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
