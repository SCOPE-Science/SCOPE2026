---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

For iid infinite-alphabet Zipf pi_i=c i^-a, a>1, gamma=1/a, nonloop ordered-pattern occurrence events have dependency neighborhoods of size three with self-overlap impossible, yielding aggregate Poisson approximation error O(1). Replacing loops at O(n^{gamma/2}), the directed expectation becomes S(t)=sum_m d(m)[1-exp(-(B/m)^a)] with B=(tc²)^gamma. Dirichlet hyperbola D(x)=x logx+(2gamma_E−1)x+O(sqrt x), Stieltjes integration and Gamma derivative give Gamma(1−gamma)c^{2gamma}n^gamma[gamma log n+2gamma log c+2gamma_E−1−gamma psi(1−gamma)]+O(n^{gamma/2}). Undirected merger has event probability 2pi_i pi_j and adjacent overlap pi_i pi_j(pi_i+pi_j), summably O(n^gamma), giving leading multiplier 2^{gamma−1}. Removing transitions at an input position yields 0<=A_r<=2 and sum_r A_r<=2T, so Efron–Stein Var T<=8 ET; geometric grid plus monotonicity yields a.s. and L² edge laws. Standard vertex occupancy gives V_n~Gamma(1−gamma)c^gamma n^gamma and the two mean-degree constants. Independent numerical grouping of divisor Poisson sums at a=2,n=10000,100000,500000 agrees with two-term approximation within O(n^{gamma/2}); finite truncated tails bounded separately. No CLT or all regularly varying laws established.

## originality

PASS

The finite-time second-order directed edge expectation and both a.s. logarithmic mean-degree constants are a distinct sharp result for Zipf sequence-generated graphs. Chen–Xie–Ying and Xie–Zhou establish range/degree laws; geometric-alphabet adjacent-pair papers have different probability decay. A general unpublished regular variation word-pattern theorem may subsume part, retained as priority risk.

## value

PASS

Sharp growth of observed edges and degrees in infinite-power-law sequence graphs is a natural network invariant; the divisor-function second-term expansion and strong-law bridge over overlapping bigrams fill a mathematical gap between fixed-degree limits and finite sample graph size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
