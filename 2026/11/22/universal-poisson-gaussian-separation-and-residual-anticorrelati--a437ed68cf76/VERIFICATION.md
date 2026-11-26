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

For an occupied original subset A, exactly I(A)=Σ_{v∈A}d_v−e(A) midpoint sites are blocked. Summing over the other sites factors the original marginal into the stated Bernoulli law Q tilted by F=(1+c/n)^e(A). For K=|A|, 0≤F−1≤(c/2n)K(K−1)e^(cK/2). Expanding ordered pairs under Q, their weights contribute at most c²e^c, and the remaining independent mgfs at most exp[c(e^(c/2)−1)], giving exactly the displayed constant. Since EF≥1, normalization costs at most E(F−1) in total variation; F≤e^(cK/2) also bounds all fixed moments of K under the actual law uniformly. Uniform nq_v=c exp(−c d_v/n)+O_c(1/n) and Σq_v²=O_c(1/n) give the marked Poisson Laplace functional and the normalized partition limit by logarithms. Independently verify joint convergence by drawing a Bernoulli(p_n) array on all m_n midpoint sites independently of A and then deleting the blocked successes to produce Y_n. The deletion count has expectation at most np_n E K=O_c(1); the normalization is asymptotic to √(βcn), so the difference is negligible while the independent full array has the binomial CLT. The exact conditional mean mp_n−p_n I(A) gives the raw covariance: the internal-edge term tends to zero by uniform third moments; the other term uses uniform integrability of products of Poisson mark integrals (bounded by K²) and np_n→c. The Poisson covariance is ∫t c e^(−ct) μ(dt), giving the stated negative limit. With μ=δ_ρ, differentiating c e^(−ρc) verifies the unique maximum at 1/ρ of the limiting mean, not a finite-size extremum claim.

## originality

PASS

General hard-core partition identities, Poisson approximation, and joint Poisson–normal limits with residual covariance in other models are antecedents. The verified distinct package here concerns equilibrium occupation of the two vertex populations of a one-subdivision, with a graph-uniform labeled TV estimate, degree-profile intensity and explicit negative raw covariance across arbitrary dense hosts in scope. The examined earlier statements do not give this package.

## value

PASS

The model separates rare original-site occupancy from bulk midpoint occupancy without requiring graph symmetry. The marked law captures degree heterogeneity, and the nonzero raw covariance shows what disappears under Gaussian-scale independence. These are natural equilibrium observables; the explicit uniform bound and partition correction make the mechanism quantitative without implying a phase transition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
