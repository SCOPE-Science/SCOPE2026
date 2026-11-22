---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

The norm-sum cubical join has maxima (T,U,1−T−U)~Dirichlet(p,q,1); conditionally one coordinate per block attains each maximum and other coordinates are independent uniform on its interval. Hence C=[(p+2)T²+(q+2)U²]/(3N), with mean from Dirichlet second moments. Independent Beta(p,q) split W=T/(T+U) and Beta(1,N) slack S give √N(W−p/N)→N(0,α(1−α)), NS→Exp(1). Conditional Lindeberg CLT for squared uniform coordinates yields noise variance (4/45)(α^5+(1−α)^5); the mean split variance is (4/9)α(1−α)(2α−1)^2, totaling (4/45)(1−15α²(1−α)²). At d=p−q~κ√N, expand exactly C=(1−S)^2[(N+4)/4+d(W−1/2)+(N+4)(W−1/2)^2]/(3N) and subtract the exact mean, giving (Z²−1+4κZ)/12−(E−1)/6; variance 1/24+κ²/9. No finite simulation substitutes for beta-Dirichlet and Lindeberg proofs.

## originality

PASS

Relevant published all-degree moment formulas for positive-coordinate multipartite stable-set polytopes and Hanner-polytopes are acknowledged as covering elementary moments and free-sum covariance machinery, but the specific conditional-statistic double-scaling non-Gaussian law was not present in the full statements read. Originality remains best-of-knowledge with an inaccessible algebraic primary paper named as a risk.

## value

PASS

The two block maxima are intrinsic canonical coarse radial coordinates; precisely at equal block sizes their linear Gaussian variance cancels and a different second-order law appears. This resolves a natural degeneracy, identifies the sqrt(N) imbalance scale, and distinguishes the full radius from conditional radial information, rather than promoting a routine moment calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
