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

In the specified k equal-size disjoint approval blocs and k seats, JR forces exactly one seat per bloc; higher EJR/PJR levels are vacuous since every group with a nonempty common approved candidate lies in one quota-sized bloc. Thus C=Σ block maxima and U=globally top k of kq, giving tail-binomial exact expectation integrals. The variational top-k representation U=min_s(ks+Σ(X-s)_+) and positive density at t=F^-1(1-1/q) yield a sample-quantile O_p(k^-1/2) band and O_p(1)=o_p(sqrt k) linearization error. Independent block CLT and delta method give the coupled deficit and ratio variances; finite second moment supports finite variance. Independent exact rational checks reproduce uniform finite deficit for 91 (k,q) cases, σ²(q=2)=1/72, σ²(q=3)=257/19440, and ratio τ²(q=2)=52/2187. The unrestricted CLT follows analytically from block independence and quantile linearization, not simulations.

## originality

PASS

Specific fairness-constrained random welfare loss, exact finite uniform formula and coupled max/top-k Gaussian variance are not present in the full accessible motivating candidate-quality paper, which emphasizes worst-case deterministic representation tradeoffs. Order-statistics theory is acknowledged as technique rather than claimed invention.

## value

PASS

The natural equal-sized party-list JR stress test quantifies the stochastic loss of a binding representation quota relative to a genuinely optimal global top-k committee. Its exact finite expectation and tight 8/9 uniform asymptotic floor for q≥2, alongside coupled Gaussian deficit and ratio variances, yield useful magnitude and uncertainty benchmarks beyond the already studied worst-case quality tradeoffs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
