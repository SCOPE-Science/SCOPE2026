---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The full tent map folding of doubling gives exactly m=2^n distinct fixed points, one in each interval [j/m,(j+1)/m], in the two interlaced 2k/(m-1),2(k+1)/(m+1) grids. Increasing 1D coupling sends each interval to its grid point and is optimal for all p>=1. Summing offsets gives W1=(2m^2-1)/(6m(m^2-1)), W2^2=1/(6(m^2-1)), Winfty=1/m; the offsets approach two uniform grids, producing limit m^p Wp^p=2/((p+1)(p+2)). Convex interval p-cost gives unrestricted m-atom quantizer lower bound 1/[2m(p+1)^(1/p)]. Independently enumerated exact inverse branches and rational W1,W2,Winfty for n=1..8. Finite verification is corroboration, while the quantile proof establishes infinite n/fixed p.

## originality

PASS

Earlier generalized tent-repeller theorem gives the same exact W1 at slope H=2 and the period-prime theorem gives a distinct exact-period bottleneck distance. Thus W1 and grid coordinates cannot be claimed new. Neither prior theorem covers the all-finite-p Wasserstein asymptotic inefficiency factor relative to unrestricted optimal quantizers, nor the exact W2^2 for all n. The distinctive p-continuum comparison survives the checked published claims; earlier optimal quantization methods are acknowledged.

## value

PASS

The exact price of using a dynamical fixed-point census rather than an optimally placed m-point quadrature/quantizer is a natural quantitative dynamical invariant; the continuum of sharp p-dependent constants, W2 identity and persistent factor gap supply a useful precise benchmark beyond ordinary equidistribution or an isolated W1 computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
