---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Each triple of nonparallel lines with Θ uniform on [0,π), signed independent N(0,1) offsets H, has area A=(s23 H1+s31 H2+s12 H3)^2/(2|s12 s23 s31|). Given angles, Z is N(0,S²), W=sqrt(P)/S<=1, and P(A<=h|Θ)=erf(sqrt(h) W)=2 sqrt(h)W/sqrtπ+O(h^(3/2)) uniformly. At h=t/n^6, mean choose(n,3)p(h) = κ sqrt(t)+O_t(n^-1) with κ=E W/(3sqrtπ). For distinct triple indicators with no indices shared independence is exact; one shared line gives joint O(h) by conditional independent remaining offsets and an AM-GM density bound; two shared lines gives O(h log(1/h)) after integrating near-parallel angular gap. There are O(n^5),O(n^4) such ordered pairs, hence the Chen–Stein b1/b2 sums are O_t(1/n), proving Poisson count TV and minimum Weibull. For one rare triple B has rank2, c=(s23,s31,s12) is null vector, H=BX+(c/S)V with V~N(0,1) independent of X|B~N2(0,(B^TB)^-1); normalized Q_h=V/(sqrt(2h)W) on A<=h has joint density proportional W exp(-hW²q²), giving W-tilted directions and independent asymptotic Uniform(-1,1) defect in total variation with the exact conditional Gaussian X. Independent Cartesian line-intersection/area checks on 100 nonparallel triples and separate nested adaptive quadrature E W=0.34818544803748, κ=0.06548086764189 agree at numerical precision; finite calculations are not proof of dependence estimates or TV limit. The mark statement is about one conditioned triple, not an entire marked process.

## originality

PASS

Best-of-knowledge original **nonstationary fixed-n Gaussian-offset** small triangle law with explicit intensity, O_t(1/n) Poisson approximation, and conditional angle/location/signed-defect disintegration. Schulte–Thäle establish square-root Weibull and Poisson mechanism for **stationary Poisson lines in a bounded window**, which is properly credited; another contemporaneous independent-line theorem gives the opposite, large-area near-parallel Pareto tail. Neither implies this ensemble-specific coefficient or the rare-event spatial mark.

## value

PASS

Extreme small triangles in an explicitly sampled iid line arrangement are a natural stochastic-geometry observable. Exact Poisson intensity, rate, and conditioned geometry distinguish close concurrency from near parallelism, enabling quantitative rare-event localization; these are motivated invariants beyond the classical Weibull exponent. The exact spatial/angular mark law gives a distinct useful disintegration and is not just numerical quadrature of κ.

The dated certificate retains the supplied scientific assessment, sources and limitations.
