---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

PASS. The pinned source's diagonal derivative bookkeeping gives q_(B_j+t)=gamma^m(1-(-gamma)^j)/(gamma+1)+(-1)^j t and ||DF^n v||^2=exp[n(a+b)](alpha^2 exp[(a-b)q_n]+beta^2 exp[-(a-b)q_n]) for alpha beta!=0. Taking the dominant exponential yields |Z_n-|q_n|/n| <= const/n; any finite prefix is histogram-negligible. Since B_j/ell_j→1/(gamma-1) and q_(B_j)/((-1)^j ell_j)→-1/(gamma+1), uniform within-block scaling gives h(u)=|u-c|/(u+d). The weighted Riemann sums prove mu_theta=(d h_#Leb+int_0^theta delta_{h(u)}du)/(d+theta), and compactness of theta proves exhaustion of ALL weak cluster laws; the endpoint representations coincide. Inverting h gives the exact G(t) and G_c(t)-G(t)=t(s-t)/(1-t^2)>0 for 0<t<s. Independently checked 75 exact rational parameter/threshold identities; finite checks support, not replace, the limit argument. Correct only on the specified regular wandering rectangles with allowed source parameters and both tangent components nonzero.

## originality

PASS

PASS within examined statements. Nakano–Soma–Yamamoto (2022) already prove the existence of the wandering rectangles, exact geometric derivative products and an interval of pointwise finite-time Lyapunov accumulation values. Their Theorem 3.1 does not classify empirical probability laws over observation times; an accumulation interval alone mathematically cannot determine frequencies. A published November 1 related result determines coordinate-axis *Cesàro scalar averages* and a logarithmic regularization; its full RESULT was read and does not yield this probability-valued family as a stated implication. The new contribution is the complete one-parameter time-histogram weak-cluster family and rational CDF contrast, not the known derivative identities. This is a short deduction from strong prior input; other formulations in uninspected journal appendices and unindexed literature remain an explicit priority risk.

## value

PASS

PASS. On a positive-area family already known to be Lyapunov-irregular, the natural quantitative question is how often successive finite-time rates occupy different subintervals, not just what values accumulate. The complete phase-parametrized weak probability measures, exact rational block-end CDF and strict within-block contrast distinguish observable time-frequency behavior that pointwise accumulation intervals and a single Cesàro average do not determine. This is an independently useful invariant for the motivating example, despite being a specialized and relatively short calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
