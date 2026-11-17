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

Proof reconstructed from exact stationary-sleeper first-hit representation in Junge–Kaufman–Meisel Proposition 5. Bernoulli refresh preserves independent Bernoulli(p) stationary coordinates even conditional on sink choices; independent exact checks show birth u=(1-q)p(1-y/n), death d=(1-q)(1-p)y/n, drift -(1-q)(y-np)/n, center second moment ->2p(1-p). At t_n=(1-p)n/q_n and time windows n*s, martingale diffusion scaling gives stationary OU, jointly independent sink-count Gaussian G; fluctuation of Z across n steps vanishes on sqrt(n) scale. Doob and binomial-refresh subgaussian maximal bounds localize the first hit from both tails; nondegenerate OU immediate crossing enables hitting-time functional continuity. Distribution at hit equals -(G+c tau)/sigma; shifting the time boundary and reversing stationary OU cancels G, yielding sup_t(X_t-(c/sigma)t). Endpoint path properties follow linear penalty, OU Gaussian increments/ergodicity. Finite checker script examined, but no finite experiment is asserted to prove functional CLT, independence, localization or continuum law.

## originality

PASS

Best-of-knowledge critical-window model-specific limit not established by inspected original ARW paper; its exact representation and far smaller sink Gumbel asymptotic are prior, while the finite c OU supremum limit requires new moving-boundary analysis.

## value

PASS

The finite nonzero critical sink parameter is an explicit open scaling gap between known stationary Gaussian and Gumbel regimes in a natural interacting-particle model. Identifying a nontrivial continuously parameterized OU-supremum crossover has independent mathematical relevance and could inform future asymptotic and finite-size studies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
