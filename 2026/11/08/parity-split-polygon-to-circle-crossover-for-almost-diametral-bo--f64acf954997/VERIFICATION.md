---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For unit-circumradius regular n-gons, the polar boundary parametrization has vertex directions at integer angular coordinates, radius r_n(u)=cos(pi/n)/cos((pi/n)(1-2 dist(u,Z))) and arclength density pi*cos(pi/n)/(n*sin(pi/n)*cos((pi/n)(1-2dist(u,Z)))^2). Opposing directions have phase shift sigma=0 for even n and 1/2 for odd n. Expanding the cosine-rule chord deficit at angular separation pi+2pi v/n gives pi^2[n^-2][2q(u)(1-q(u))+2q(u+sigma+v)(1-q(u+sigma+v))+v^2]+O(n^-4) locally. Positivity localizes v to bounded intervals for fixed t; dominated convergence gives n P(D>2-pi^2t/n^2)=H_sigma(t). Piecewise-affine corner geometry yields even H_0(t)~t^2/2 and odd hard cutoff H_1/2(t)=0 for t<=1/4 and 16(t-1/4)^2/9 opening. 0<=f<=1/2 proves circular square-root envelope H~2sqrt(t) as t grows. Minor normalization wording in the original proof calls integer directions side normals, although its displayed radius puts *vertices* there; this is a harmless coordinate-description slip, not a change in any formula or theorem. Six independent finite-n vs limit quadratures reproduce agreement, and finite checks do not prove the limit.

## originality

PASS

Earlier regular-polygon distance literature concerns invariant-line chords or two interior-area-uniform endpoints; its CDF cannot be substituted for independently sampled perimeter-arclength endpoints. Published polygon short-chord coefficients concern D near zero, whereas this is n-dependent near-diameter probability. Lao-based maximum sample diameter at fixed odd polygon has different sample-count and extremal ordering. The explicit parity-split n^-2 boundary-chord scaling and local onset do not follow from those theorems. No exact or stronger matched result located; historical priority provisional.

## value

PASS

This is a natural critical double scale for boundary chords as regular polygons converge to a circle, where isolated versus flat antipodal maximizers and parity lead to qualitatively different threshold behavior. The explicit H_sigma integral, hard odd gap and sharp onset coefficients encode useful geometry beyond a small finite example; the result is an analytically proved asymptotic invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
