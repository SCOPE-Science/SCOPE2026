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

After the first attachment, degree-two vertices are nonadjacent; an attachment promotes any such endpoint and creates one new degree-two vertex. With M=2N−3, incidence probabilities for the root, a degree-two vertex and a degree-two root neighbor are D/M, 2L/M and 2K/M. For a root incident edge to have a degree-two endpoint, it either joins a degree-two root neighbor, or the root itself has degree two, accounting for K+2J rather than K. The root stays of degree two with probability 1−2/M at each step while J=1; starting at P(J_4=1)=1/3 gives E J_N=1/(2N−5). At N=4, the root has degree three and two degree-two neighbors in two of three histories, and degree two and no such neighbors otherwise; L_4=2 deterministically. The linear recurrences for μ, ℓ and k give the displayed closed forms by substitution and that base. Expand Cov(D+I,L+1−C). Conditional expectations give Cov(D,1−C)=−2c/M and Cov(I,L)=c/M, so together with Cov(D,L) these terms give (1−1/M)c. The remaining term is Cov(I,1−C)=2μℓ/M²−(k+2EJ)/M; substitution gives the exact forcing. The lower polynomial 16N²−124N+258 is positive and increasing on integers N≥4. Dividing the recurrence by μ_(N+1) produces a convex update toward a target tending to 1/12 with divergent total update weight, giving c_N/√N→√π/12. The marginal scales also follow directly: E[D_N(D_N+1)]=2M by a telescoping recurrence, so Var(D_N)∼(4−π)N; total conditional variance for L gives v_(N+1)=(1−4/M)v_N+2ℓ/M−4ℓ²/M². Since ℓ/M→1/4, averaging for v_N/N has step weight asymptotic to 3/N and target 1/12. These yield the stated correlation constant. Fresh exact enumeration of all labelled histories (extend each history along each current edge, with equal weight at fixed N) through N=8 gave covariances 0, 2/75, 46/735, 94/945, 1030/7623 at N=4–8, matching the recurrence. The frozen checker was not run.

## originality

PASS

The supported increment is the exact mixed covariance, its sign and its leading constant in the fixed HSC(2) growth process. The model and marginals are credited. A close analogous covariance in a preferential-attachment tree is acknowledged; neither that indexed theorem nor the available descriptions of the same-model literature give this mixed statistic. Full-text access limitations remain.

## value

PASS

Measuring the oldest vertex jointly with the global degree-two boundary answers a natural dependence question that both marginals leave open. The exact finite positive sign and the growing covariance with decaying correlation distinguish absolute dependence scale from normalized dependence. The special mixed-incidence correction also has structural content; omission changes finite covariances.

The dated certificate retains the supplied scientific assessment, sources and limitations.
