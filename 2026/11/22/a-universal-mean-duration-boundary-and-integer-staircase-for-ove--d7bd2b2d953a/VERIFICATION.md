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

A start in a silent gap of length g escapes capture on a phase set of mean length E[(g-L)_+]. Thus PQ=P-sum_i E[(g_i-L)_+]=A+sum_i H(g_i), also for events long enough to wrap around the circle. Increasing A at fixed n by shortening any gap strictly improves capture, since 1-S(u)>0 for u>0. Full budget leaves A=B-n*h>0 and total gap c+n*h; strict concavity of H gives exactly the equal-gap equality cases, independent of the allocation of active lengths. The derivative of the relaxed numerator is M_h(h+c/x)-h, with M_h(g)=H(g)-(g-h)S(g), M_h'(g)=(g-h)f(g)>0, and limit m, since g*S(g)<=2*integral_(g/2)^g S(u)du tends to zero. This settles strictness at h=m and identifies d_h when h<m. Each adjacent difference has derivative S(h+c/(n+1))-S(h+c/n)>0, limits H(h)-h<0 and m-h, and is strictly decreasing in n at fixed c by strict concavity of the count envelope. This proves the ordered roots and exact adjacency ties; the mean-value theorem traps c_n strictly between n*d_h and (n+1)*d_h. The asymptotic uses the same root equation for unbounded mathematical n, independently of the finite feasible prefix at any fixed budget. N=1 and the excluded zero-length count when B/h is integral are consistent. Independent substitution of H=1-exp(-g) and ranking n=1,...,15 reproduces n=5, Q_5=0.7614450862358281 and Q_1=0.7074075836218131 (runner-up n=6 with 0.7609650547093678).

## originality

PASS

The survival-gap functional is known and fixed-count balancing is a direct consequence; neither is credited as distinct in isolation. Credit the exact distribution-universal mean-duration cost boundary with its equality and sharpness, and the precise all-count ordered transition rule in the cyclic, energy-budget model. The two close indexed models each overlap a substantial component, but the inspected claims and restrictions do not jointly or separately entail this classification.

## value

PASS

The energy constraint makes splitting live time neither free nor always beneficial. An exact all-law cutoff in measurable event-duration units and a global integer choice including ties give a usable design classification, not just a fixed-count balance or numeric comparison. It locates the costs at which experimental scheduling decisions change and separates the count restriction from the timing-law thresholds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
