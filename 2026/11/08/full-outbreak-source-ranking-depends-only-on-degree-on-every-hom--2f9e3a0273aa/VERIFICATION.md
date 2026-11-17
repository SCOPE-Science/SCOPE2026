---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

On a finite undirected tree (n>=2) infected from source s, the unique rooted paths imply that every vertex becomes infected iff each parent sends to every child. Conditional on T_v, independent outgoing contacts make this event probability X_v^c_v, so independence across v gives product_v m_c_v. Because c_s=d_s and c_v=d_v-1 otherwise, P_s=(product_v m_(d_v-1))*m_(d_s)/m_(d_s-1). Moment log-convexity proves ratios increasing, strictly for nonconstant positive T; the degree-2/degree-1 ratio is m2/m1^2. The beta integral for exponential T gives m_j=j!lambda^j/product_(i=1)^j(mu+i lambda). Independent rational two-point infectiousness check with X=1/4 or 3/4, equally likely, confirmed two nonisomorphic six-vertex trees with degree multiset (3,2,2,1,1,1) produce P_degree1=5/128, P_degree2=25/512, P_degree3=7/128; the ratio equals 5/4. Finite checks support rather than establish the exact all-tree theorem.

## originality

PASS

A best-of-knowledge exact joint complete-outbreak identity for iid arbitrary infectious lifetimes, ranking by source degree only. Karrer-Newman tree epidemic message passing and Sharkey/Hall-Siebert exact node marginal equations supply the model and machinery, but their inspected core statements give probabilities of specified nodes and not the explicit joint event/all-transmissions product, degree-quotient, or heterogeneity ratio. Derivation uses familywise correlations from one parent lifetime; the claimed distinction is not generic independent-bond percolation. A hidden earlier cluster/all-edges-success coefficient in broader epidemic literature remains a priority risk.

## value

PASS

The precise all-vertex outbreak event is a meaningful rare-event epidemic risk quantity distinct from expected or peak burden. An exact topology-blind source-degree ordering, robust to arbitrary iid infectious-time heterogeneity, and heterogeneity-measuring risk ratio give a structural fact a network researcher could use for verification and risk comparisons. The conditional factorization is short, but concerns correlated outgoing edge outcomes, not a mere relabeling of independent-bond formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
