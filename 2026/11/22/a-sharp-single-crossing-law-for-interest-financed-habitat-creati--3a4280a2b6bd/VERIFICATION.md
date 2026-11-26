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

For a deterministic date s, solve P'=q−(q+μ)P with P(0)=0, then set q=ae^(rs), t=H−s and y=q+μ. This gives F(s)=q(1−exp(−yt))/y. Differentiating with q'=rq and t'=−1 gives F'=q exp(−yt)(rB−1). To check the critical strict inequality independently, put x=yt, p=μ/y and z=exp(x)−1. Then yB=(1−p)x+pz, B_t=1+pz, and yqB_q=p(1−p)[(x−2)z+2x]. Expanding gives y(B_t B−qB_q)=p²z(z+1)+p(1−p)(3z−x)+(1−p)²x>0 for t>0. Thus at any zero of G(s)=rB−1 before H, its derivative is strictly negative, using r=1/B at the zero. With G(H)=−1, two downward zeros would force an intervening non-downward zero, which is impossible. At r=r_c the endpoint zero itself has negative derivative. This proves uniqueness in both regimes including r=0, without assuming that G is globally decreasing. The identity B=t+μ∫₀ᵗ(t−u)exp((q+μ)u)du proves strict decrease of r_c in a,μ,H and r_c<1/H. The no-extinction expression reduces to maximizing ae^(rs)(H−s) and gives the stated comparison. Independent bisection for a=μ=H=r=1 gave s*=0.364045975707 and occupancy 0.464936881234 versus 0.432332358382 at zero, with r_c=0.476811688088. At r=0.6 with those other parameters, delay still wins, directly illustrating the sub-unit rH regime. RESULT.md, VERIFICATION.md and check.py were inspected, not executed; the finite 4,498-check run is reported by the frozen verification file, not an independent certificate. All conclusions are for a single initially empty created patch with fixed rates after creation and a terminal occupancy reward.

## originality

PASS

The bounded evidence supports the distinct exact result for an empty target with exogenous colonists and fixed-rate recolonization after creation. The most relevant published offsetting work already studies interest-financed delay and gets credit for that timing concept; its stronger possible relation to this special case remains unresolved because the full paper was inaccessible. The actual closest indexed statements do not give the optimizer or comparative statics. This is not a priority verdict on interest-financed timing generally.

## value

PASS

With a fixed census, interest improves later colonization while waiting removes occupancy time, and even this one-target tradeoff is not decided by a general first-order condition alone. The exact unique-optimum classification isolates the effect of extinction: increasing it strictly lowers the rate required to justify waiting, even below the no-extinction rH=1 threshold. It provides a motivated analytic benchmark separating colonization and extinction effects, without implying that delay improves spatial conservation outcomes generally.

The dated certificate retains the supplied scientific assessment, sources and limitations.
