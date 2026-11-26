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

Every labelled state can reach the same cyclically reset configuration by copying fixed zealots in other parts; finiteness gives one closed class, without claiming irreducibility on all labelled configurations. Counting flexible recipient and outside donor frequencies gives L X_(j,a)=((n−1)/n)Q_(j,a)−X_(j,a)+δ_(j,a)/n and L P_a=(1−rP_a)/(rn), since the mean of the Q_(j,a) is P_a. Taking expectations and solving the linear equations gives the stated finite means. Subtracting the drifts leaves a contracting term −r/(r−1) times the discrepancy plus a bounded O(1/n) remainder. Each coordinate discrepancy jumps by O(1/n) at total rate O_r(n); its stationary square estimate is O_r(1/n). Conditional on a part and the configuration, donor and flexible-recipient opinion frequencies multiply, so in stationary L¹ the rn-scaled jump covariance is 2(diag(P)−PPᵀ)+o(1), not diag(P)−PPᵀ. The accelerated third-order Taylor error is O(1/n), and the factor 1/2 in Taylor yields diffusion coefficient one. For a monomial of degree K, the resulting stationarity equation is K(K+r−1)m_k=∑_a k_a²m_(k−e_a). Its unique normalized solution is the uniform Dirichlet moments, determining the law on the compact simplex. The L² discrepancy passes the convergence jointly to the whole matrix, with every row the same random vector. An independent rational solve of the 27-state update-attempt transition matrix (/workspace/review-evidence/replay.py 1; output 1.txt) gives the entire supplied stationary vector and all ten probabilities, not just a sampled check. Even a symmetric Dirichlet–multinomial with arbitrary common concentration cannot fit: p_(2,1,0)/p_(1,1,1)=13/11 forces concentration 11/15, which predicts a different p_(3,0,0)/p_(2,1,0) than 46/39. Only the stationary equal-part, fixed-r setting is concluded.

## originality

PASS

The supported increment is the joint synchronized stationary limit for this multipartite frozen-site model, alongside the exact finite means and a finite obstruction for the count law. Uniform Dirichlet laws and Wright–Fisher limits are not new, and a closely related general voter-to-Fleming–Viot theorem supplies the applicable framework. Its common mutation measure, however, is not the part-dependent law obtained by deleting the zealots, and its empirical measure does not resolve part discrepancies or finite composition probabilities. The inaccessible 2026 Moran article is an explicit residual risk, not used as evidence for or against coverage.

## value

PASS

The theorem identifies a structural separation between exact finite stationarity and its macroscopic limit when a positive fraction of possible edges is deleted. Complete loss of within-part interactions produces a finite non-Dirichlet–multinomial count law yet leaves a shared nondegenerate uniform simplex limit, with a quantified partwise synchronization estimate and all moments. The small exact chain is useful as a counterexample to extrapolating the complete-graph finite result, rather than an unmotivated tabulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
