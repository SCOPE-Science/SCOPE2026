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

An A-source can cover exactly one new B vertex until its quota b is met, and conversely. Thus completion by t is exactly b≤S_t≤t-a with S_t∼Bin(t,q), and no t<N qualifies. At time N one quota is filled, the other has deficit |S_N-b|, and the extra mean is the deficit divided by the future opposite-source probability. For q_N=β_N+u_N/√N with u_N→u and t=N+floor(r√N), the centered binomial (S_t-b_N)/√N has limiting mean u+rβ and variance αβ, giving the displayed CDF for r≥0 (no atom at zero). The finite mean identity converges by the same triangular-array limit and uniformly bounded second moments of (S_N-b_N)/√N. At q=β_N this yields an O(√N) excess by Cauchy–Schwarz. The lower bounds b_N/q and a_N/(1-q) diverge at the endpoints and, at any minimizer, force |q-β_N|=O(1/√N). Along each convergent scaled subsequence the mean limit applies and comparison against every fixed shift forces the same minimizer: F′(u)=Φ(u/σ)/α-Φ(-u/σ)/β, strictly increasing, with root σΦ⁻¹(α) and F there equal to φ(Φ⁻¹(α))/σ. This does not assume exact finite-size uniqueness. At uniform vertex weights the binomial L¹ law gives the claimed linear ratio for unequal limiting parts. The uploaded checker was inspected, not executed; its recorded 1,470 exact checks cover finite strip probabilities and means only.

## originality

PASS

The finite probability problem is the classical later waiting time for two Bernoulli frequency quotas, not a new stopping-time formulation. The supported distinct contribution is the growing-quota local completion profile together with the sharp all-minimizer expansion for the mean under fixed independent weights. In the examined evidence, neither finite quota laws nor the known normal critical-fractile computation alone establish the full asymptotic optimizer theorem.

## value

PASS

Complete bipartite graphs isolate a natural source-design question with no dependence on tie-breaking at neighbors. Reweighting reduces the linear excess of uniform vertex sampling to order √N at unequal limiting proportions; within this best scale, the nonzero quantile correction strictly improves the leading excess coefficient over exact quota balancing. The asymmetric completion profile determines deadline probabilities for all local weights, independent of the mean criterion. This is informative for the fixed i.i.d. design family without claiming superiority to adaptive or periodic schedules.

The dated certificate retains the supplied scientific assessment, sources and limitations.
