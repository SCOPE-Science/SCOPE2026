---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Normalized adjacency Fourier fiber is [[2 cosθ/3,1/sqrt3],[1/sqrt3,0]], with eigenvalues (c±sqrt(c²+3))/3 and normalized positive lower-band u(c). Spectrum of normalized Laplacian is [0,2/3]∪[4/3,2]. For 0<ω≤4/3 the spectral subspace has fiber dimension one almost everywhere, and the frame multiplier is |<w,u(c)>|². The two endpoint vectors v,q have positive overlap s<1; averaging their squared projections upper-bounds any sensor by (1+s)/2, attained uniquely by normalized v+q. The traversed positive eigenvector arc gives the entire-interval bound. A complex row has constant multiplier for all c exactly at unit quadrature sensors (1,±i)/sqrt2; above 4/3 both eigenmodes appear on positive-measure fibers and any 1×2 row has a kernel. Independent Fourier-fiber numerical checks at ω=.05,.25,1,4/3 match sharp endpoints and verify the constant half-energy multiplier; these do not prove the infinite graph result.

## originality

PASS

Generic graph Paley–Wiener sampling and subspace sampling theory covers the framework, but checked source statements did not solve the particular two-site complex-row optimization and tight-sensor classification on the infinite normalized pendant graph. Closest directly motivating 2026 manuscript is inaccessible beyond its abstract; this remains a concrete originality priority risk, not an automatic failure.

## value

PASS

This is an exact and practical E-optimal one-number-per-cell sensor design, classification of all tight sensors and a sharp sampling bandwidth phase transition on a canonical periodic decorated graph; it distinguishes optimally stable sensors from exactly tight but suboptimal sensors. Exact two-band cutoff and equality conditions go beyond generic sufficient sampling-set criteria.

The dated certificate retains the supplied scientific assessment, sources and limitations.
