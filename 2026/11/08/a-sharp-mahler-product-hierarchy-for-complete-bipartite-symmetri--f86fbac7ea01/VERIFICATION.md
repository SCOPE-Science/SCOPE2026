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

The primal root-polytope is a two-opposite-face join; orthogonal section integration yields 2sqrt(N)/[(p-1)!(q-1)!] times integral A_(p-1)A_(q-1). For the polar |u_i-v_j|<=1, anchor minimum left value at zero, integrate left block max M with right interval length 2-M, and divide anchored volume by sqrt(N), giving 2^(N-1)p!q!/[sqrt(N)(N-1)!]. The density B_r=r A_(r-1)/2^(r-1) integrates to one; the known h-star identity also gives the finite sum. A_(r-1) is a polynomial with nonnegative coefficients in h=t(1-t), B_1=B_2=1, B_r strictly increasing for r>=3. Strict Chebyshev covariance gives R>1 iff p,q>=3 and MLR of successive B_r gives strict coordinatewise monotonicity. The B_q order-statistic mixture weakly concentrates at 1/2 as q diverges; the fixed-p limit and sqrt(min)-order growth bound follow by elementary concentration/Cauchy-Schwarz. Independently recomputed 64 exact beta-integral overlaps and the h-star finite sum for 1<=p,q<=8, applicable monotonic inequalities, and R(3,3)=81/80; no infinite claim inferred from those checks.

## originality

PASS

IMPORTANT qualification: neither the primal-volume formula (Higashitani–Jochemko–Michałek 2018) nor the polar-volume formula is novel: the published 2026-10-18 complete-multipartite Lipschitz-dual volume identity at t=2 gives exactly the anchored K_(p,q) polar volume (numerically and algebraically cross-checked). The genuinely surviving originality is the Mahler overlap-density structure, the rigid equality iff min<=2, strict normalized-product monotonicity in each nontrivial class size, and the two-parameter sqrt(min) growth/finite fixed-class limit. These comparisons were not claimed by the inspected older sources.

## value

PASS

The strict threshold min(p,q)<=2 and strict Mahler hierarchy establish a natural shape-ordering in a canonical family of graph-root bodies, connecting volume-product geometry to stochastic overlap monotonicity. The sqrt(min) asymptotic distinguishes fixed-class and jointly growing regimes and is a genuinely motivated geometric comparison even though component volume formulas are known.

The dated certificate retains the supplied scientific assessment, sources and limitations.
