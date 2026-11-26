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

Root the circular gaps at one labeled sampled point (the statistics are cyclically invariant). Relative positions of the other points are iid uniform, so dividing iid exponentials by their independent Gamma sum gives the correct gap law. The Gamma second moment yields (1); order increments of rates 3,2,1 give the stated means, covariance 13/36 and normalized −1/81. For the large-n result, using Bernoulli states 0,1 with rows (1−p,p),(1−p,0) gives the cyclic trace formula. Conditioning on A≤u shifts the exceedance probability from p to (p−q)/(1−q) when u≥v. In centered coordinates, Taylor expansion of the positive eigenvalue gives log λ+=−p²+O(p³), (log λ+)'=−2p+O(p²); the other eigenvalue and its differentiated power are negligible locally when p=exp(−y/2)/√n. This gives the positive pointwise CDF residual in (6). For a direct tail check, differentiating the Bernoulli event by pivotal sites gives |R'_n(s)|≤2ns(1−s²)^floor((n−3)/2): pivotality needs an occupied neighbor and no adjacent successes among a disjoint matching after deleting the site and its two neighbors. Thus when p≤1/2 and q≤p/2, p'∈[p/2,p] and the scaled residual has integrable majorant C exp(−x−y/2−e^(−x)−c e^(−y)). Under dp dq/(pq), p/2<q≤p costs O(1/n) by e^(−np/2) n p²; q>p costs O(1/n) by integrating e^(−nq) n p² first in p. For p>1/2, q≤1/4 use p'≥1/4 and the same pivotal bound times p−p'≤q, integrable in u; if q>1/4 the domain is bounded and F_A is exponentially small. The factor 1/2 in the Jacobian cancels the differentiation factor 2, giving Γ(1)Γ(1/2)=√π. The Gamma normalization correction is O(log²(n)/n)=o(n^(−1/2)) before division by n(n+1). This proves the stated sign reversal without a unique crossing or cutoff claim. Inspected check.py and VERIFICATION.md but did not execute the upload; their finite-domain quadrature does not certify the limit.

## originality

PASS

The spacing representation and cyclic no-run calculation draw on classical methods. The exact negative small-sample value together with the order and coefficient of the mixed residual are not covered by the inspected results for sums, threshold counts, or first-order extreme limits.

## value

PASS

The two statistics naturally distinguish one long empty arc from simultaneously long neighbors. Neither a first-order Gumbel law nor the sign for n=3 predicts the leading residual after normalization. The exact sharp √π term and opposite signs answer a meaningful dependence question, rather than merely adding a small-size covariance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
