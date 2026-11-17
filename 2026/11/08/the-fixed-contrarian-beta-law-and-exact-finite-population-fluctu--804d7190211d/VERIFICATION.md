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

For every m,r>=1 the four specified positive pair-count jump rates make a finite irreducible reflection-symmetric Markov chain. The generator gives LX=mY-rX and LY=-rX-mY and three stationary quadratic moment equations; independently derived and solved to obtain Var(A/m)=(m+3r)/(4(2mr+m+r)), Cov(A/m,B/r)=(r-m)/(4(2mr+m+r)), Var(B/r)=(3m+r)/(4(2mr+m+r)). For fixed r, scale A/m: fast conditional B chain has unique Binomial(r,1-x) equilibrium including absorbing endpoints; the slow marginal stationary generator r(1-2x)∂+x(1-x)∂² yields Hausdorff moments (r)_k/(2r)_k and hence Beta(r,r). Bounded generators and compactness justify the weak joint limit; finite checks only corroborate.

## originality

PASS

Masuda 2013 model 1 already gives Gaussian large-both-population fluctuations and the r=1 uniform share limit, both explicitly excluded. Sections III.B/C of the primary original paper do not supply the exact all-finite-m,r covariance or joint fixed-r>=2 Beta(r,r)–Binomial limit. Other noisy-voter/zealot beta laws have different transition generators and do not mathematically imply these model-1 formulas. Best-of-knowledge originality retained with residual priority risk.

## value

PASS

Fixed-r contrarians are a natural non-Gaussian singular limit of Masuda’s voter dynamics; exact finite covariances plus complete joint weak limiting law are substantive reusable stochastic-process invariants, not a routine restatement of the known r=1 case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
