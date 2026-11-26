---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The same-label coupling keeps the clock independent of each nondistinguished label stream. Conditional on T=t, the other clock count has mean t and variance 2t by the Poisson–gamma calculation. Conditional on both lengths, the mismatch can occur only if an extra draw hits any label absent in the shorter prefix, at cost ≤|T−N|(x^T+x^N), x=1−1/n. The geometric-phase transform has shift n(1−w)/w. At z=x² this is at least 2; at w=(2−z)^−1 it is 2−1/n. The exact shift-two product is 2/[(n+1)(n+2)], and the smaller shift increases the product by at most e² (bound each negative log by 1/[n(h+2)−1]). With E(T−N)²=2nH_n, Cauchy–Schwarz gives the stated per-coordinate coupling cost. Independent Poisson thinning gives U=e^(−S/n) distributed Beta(1,n); conditional on U the peers have independent Bin(n,U) laws. Coupling binomials to Poisson variables costs at most nE[U²]≤2/n per peer. Shared coupling U=1−exp(−E/n) and superposition cost at most E[E²]/(2n)=1/n per peer. All error costs apply jointly by union bounds, and integrating the shared exponential gives the reported negative-multinomial mass and geometric sum. No independence across peers is assumed after averaging the clock. Bound is a sufficient regime, not a threshold. Inspected frozen verify.py without executing it; its exact half-atom is for the continuous comparator, not the discrete law, which can have ties.

## originality

PASS

The model of independent competing coupon collections and the mixed-Poisson/negative-multinomial law are classical ingredients. The distinct contribution supported by the comparisons is a quantitative coupling of the synchronized full deficit vector at a distinguished first completion to the classical law, with uniform control for a growing number of peers.

## value

PASS

A finite joint law approximation over many simultaneously observed independent albums is useful in a way that marginal geometric convergence is not: it quantifies the common stopping dependence and gives an explicit growing-dimensional error budget. The proof addresses a natural stopping statistic, without claiming its sufficient dimension scale is optimal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
