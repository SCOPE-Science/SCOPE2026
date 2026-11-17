---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For the actual Cayley join of a[-1,1]^d at z=0 and bB_1^d at z=1, horizontal z-sections are sB_infinity+tB_1 with s=a(1-z),t=bz. Coordinatewise clipping proves membership exactly when sum (|x_i|-s)_+<=t. Decomposing by k external coordinates and orthants yields volume 2^d sum_{k=0}^d binom(d,k) s^(d-k)t^k/k!, with no missing sign or factorial. Beta integrating each z^k(1-z)^(d-k) term produces total volume 2^d a^d H_d(rho)/(d+1), and the conditional height is exactly Beta(k+1,d-k+1) with normalized truncated-Poisson weights rho^k/(k!H_d(rho)). Since N_d=>Pois(rho) and d*Beta(k+1,d-k+1)=>Gamma(k+1,1), a tight-mixture argument gives E0+sum_{1}^{Pois(rho)}Ei with density exp(-rho-t)I0(2sqrt(rho t)), transform (1+s)^-1 exp(-rho+rho/(1+s)); beta moments imply limits 1+rho and 1+2rho. Independent rational normalization/moment checks for (d,rho)=(3,1/2),(6,2),(12,3/2) agree. Fix rho>0 as d grows; no claim for varying rho.

## originality

PASS

Best-of-knowledge the exact finite *height distribution* of a uniform-volume point in this naturally aligned cube–crosspolytope Cayley join, and its fixed-rho Poisson–gamma/Bessel non-Gaussian limit, are not established by identified published Cayley-sum IDP papers, general mixed-volume literature, or relevant Resultary findings. Classical mixed-volume section polynomial is acknowledged; knowing its algebraic volume expansion does not alone state the normalized beta mixture and high-dimensional probabilistic limit. Full text of a plausible but not same-object Cayley paper was inaccessible; this is recorded as residual risk rather than automatic scientific failure.

## value

PASS

The height of a volume-uniform point in a canonical interpolation between two dual norm balls is a natural geometric probability invariant, and its order-1/d localization, exact beta-mixture structure, and non-Gaussian Bessel law provide a precise asymptotic classification not supplied by a table or arbitrary numerical slice. The proof uses elementary mixed-volume/beta calculations, but the resulting joint exact sampler and high-dimensional limit are separately useful. No downstream theorem or large-size generality is required by this value standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
