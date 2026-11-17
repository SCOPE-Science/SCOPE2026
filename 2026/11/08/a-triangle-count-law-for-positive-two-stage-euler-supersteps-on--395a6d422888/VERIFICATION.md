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

Directly reconstructed P=(I-h2L)(I-h1L)=I-(s/d)L+(q/d^2)L^2, with s=dh1+dh2,q=(dh1)(dh2). Since (A^2)_ii=d, edge entries (A^2)_ij=c_ij and off-edge entries nonnegative, diagonal positivity exactly 1-s+(1+1/d)q>=0 and worst-edge condition exactly s>=(2-t/d)q. For noncomplete connected regular graph, t<=d-2, combine q<=(s/(2-t/d)) and q>=(s-1)/(1+1/d) for s>1 to get sharp s*=(2d-t)/(d-1-t). Equal stages x=y for 0<s<=4/(2-t/d), then q=s/(2-t/d) and positive roots for larger s, attain all totals. At s*, both constraints tight; q*=d/(d-1-t), discriminant (t^2+4d)/(d-1-t)^2>0 yields unique unordered positive stages and extremal stochastic P*=(A²-tA-dI)/(d(d-1-t)). On K_(d+1), h2=1/(d+1) projects onto constants regardless of h1, proving unbounded time. Independent exact rational identities verified for d,t=(2,0),(3,0),(4,1),(4,2),(6,2),(8,0); checked that provided verification program forms matrices correctly. Finite graph tests are supporting only.

## originality

PASS

The endpoint property is not stagewise strong-stability-preserving positivity or Chebyshev scalar spectral stability. Alexiades--Amiez--Gremaud established multi-Euler supertimestepping; Gottlieb--Shu--Tadmor established stagewise SSP sufficient conditions. Neither inspected statement supplies an exact nonnegative final kernel depending only on min triangles per edge or the universal regular-graph sharp maximum. Resultary found numerous Radau IIA, Gauss--Legendre and RK positivity thresholds for graph families, but not this factored two-Euler endpoint condition. Specialist Legendre STS full text remained inaccessible; best-of-knowledge priority retains explicit risk.

## value

PASS

The exact graph-local triangle invariant t classifies endpoint order preservation and determines the largest practical two-stage positivity-preserving block, including an explicit stochastic/nonbacktracking kernel and unexpected arbitrary long intermediate violation on cliques. It is a natural sharp theorem connecting graph triangles and positivity of numerical diffusion; it carefully excludes accuracy and internal-stage guarantees.

The dated certificate retains the supplied scientific assessment, sources and limitations.
