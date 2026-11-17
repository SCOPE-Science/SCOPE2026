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

Uniform empirical measure converges, h_n(u)=E_mu_n |u-X| converges uniformly to h(u)>=1/4, so conditional ordered sampled pair converges to du |u-v|dv/h(u). The empirical optimal two-median cost converges to 1/8. Sorted pair joint density q(u,v)=(v-u)[h(u)^(-1)+h(v)^(-1)] and R=4(a^2+c^2)+2b^2=1+4(s-1/2)^2+2d^2 give exact support and extrema. Independently computed polynomial conditional moment integrals N1=(34u^4-68u^3+54u^2-20u+5)/48, N2=11(2u²-2u+1)(11u⁴-22u³+15u²-4u+1)/480; obtain E R=7pi/12-4/9 and E R²=154/75. The minimum ellipse and two maximum corners with density ~4b lead to lower epsilon coefficient 4pi/(5sqrt2) and upper epsilon³/384. This is analytic, not only quadrature.

## originality

PASS

The separate Nov 8 published Resultary theorem already gives the exact conditional expected Proportional limit 7pi/12-4/9, Global Pair 7/5, and mixtures, so these numbers do not establish new priority. Its full source, read directly, concerns Gaussian fluctuations of the empirical conditional-expected Global Pair cost and three-atom law; it does not give the realized lottery-draw limit second moment or corner/ellipse event tails. EC 2010 establishes strategyproof Proportional mechanism and worst-case factor four, not these exact realized uniform-population risk laws. Novelty is restricted to ex-post fluctuation law and endpoint asymptotics.

## value

PASS

A mechanism with deterministic asymptotic expected ratio still has nontrivial one-draw user risk; its exact second moment and linear/cubic endpoint rare-event laws quantify genuinely different and practically interpretable performance. The sharp two-tail constants reveal the mechanism’s near-optimal and extreme-cost probabilities, not simply a restated expected approximation factor.

The dated certificate retains the supplied scientific assessment, sources and limitations.
