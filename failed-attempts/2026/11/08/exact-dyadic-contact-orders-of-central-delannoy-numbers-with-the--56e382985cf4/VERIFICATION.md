---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The package identifies (-1)^n D_n with H(n(n+1)) via the Legendre polynomial hypergeometric identity. Its linear and quadratic Taylor terms cancel by 2-adic log(-1)=0 and Li_2(2)=0. A tail coefficient bound and finite exact coefficient parity certificate show H(4Y)=1+64Y³(1+2V(Y)), yielding v2(D_n-(-1)^n)=3 v2(n(n+1)) for t≥2; direct mod8 handles t=1. Independent integer evaluation n=1..79 matches every stated valuation, though the infinite assertion rests on the 2-adic coefficient argument.

## originality

FAIL

FAIL: The November 2 2026 published Delannoy theorem already establishes v2(D_m-1)=3v2(m) on every positive m divisible by four, and its proof establishes an analytic 2-adic interpolation F(m)=sum_j 2^j binom(m,j)^2 with uniform coefficient control on m in 4Z_2. For every odd n≡3 mod4, m=-n-1 belongs to 4Z_2; the classical hypergeometric/Legendre parity transformation gives F(-n-1)=(-1)^n D_n=-D_n, and v2(m)=v2(n+1)=v2(n(n+1)). By density of positive 4-divisible integers and continuity/constant valuation on each open nonzero 2-adic stratum, the published sharp formula extends to m=-n-1. Its t=1 cases follow by elementary mod8. Thus the new all-index alternating-sign law is a corollary of the earlier sharp even-index theorem plus standard 2-adic interpolation, with the same quadratic/cubic cancellation mechanism. The restricted cubic-contact description is likewise implied by the prior proof’s uniform coefficient parity bounds after x=4Y, not an independently motivated new invariant.

## value

FAIL

FAIL: The striking cubic dyadic valuation conjecture was already settled in the exact same Delannoy family by the earlier November 2 theorem. Recovering the odd signed indices through Legendre parity and 2-adic reparameterization is a useful observation but too mechanical to count as an independent mathematical gap; new coefficient packaging does not change that coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
