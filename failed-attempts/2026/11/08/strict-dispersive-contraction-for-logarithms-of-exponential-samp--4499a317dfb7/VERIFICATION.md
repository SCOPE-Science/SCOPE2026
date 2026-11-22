---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

Direct inversion gives Q_r(u)=log[-log(1-u^(1/r))]. With a=-log(u), w=1-exp(-a/r), g(t)=(-log(1-t))/t strictly increasing via its positive integral derivative, Q_r'(u)=g(w)/[a*u*g(1-w)]. Increasing r strictly decreases w, hence the ratio and Q'(u); integration on every compact [u,v] subset (0,1) gives strict contraction. For D=Q_s-Q_r, D is strictly decreasing; its centered version has zero integral and positive every proper initial integral, giving strict centered convex order by the equal-mean integrated-quantile theorem, including strictly convex losses. Exponential left and double-exponential right tails guarantee all finite moments. Independent stable analytic-versus-finite-difference and grid checks passed 1,936 assertions (8 shapes, 11 quantiles), supplementary only; the universal assertion is proved analytically.

## originality

FAIL

The complete real-parameter strict interquantile contraction is stated and proved verbatim in the earlier 2026-10-18 Resultary theorem for the identical CDF F_a(y)=(1-exp(-exp(y)))^a and quantile Q_a(u). A separate 2026-10-12 theorem had already proved the same all-positive-real dispersive ordering. Centered convex order and strict expectations for strictly convex losses follow automatically from the already established strict dispersive order for these integrable laws, via the centered quantile-difference and integrated-quantile criterion; the nominal addendum is not independent new mathematics. The 2026-11-08 sharp transport theorem further bounds integer-parameter ratios between n/m and 1. Therefore the final submitted theorem is prior-covered, regardless of nomenclature and distinct proof kernel.

## value

FAIL

The exact object and all real-shape quantile comparisons are natural and intrinsically worthwhile, but they were already proved in full in an October 2026 published theorem, with an even earlier separate October result. The centered convex-order conclusion is a standard direct corollary of already established strict dispersive order, not a new classification or independently useful invariant. The alternative normalization g and 1,936 finite diagnostics add no surviving mathematically motivated new claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
