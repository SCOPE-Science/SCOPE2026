---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Stable-set polytope product under disjoint union and convex free sum under graph join; in the free sum, radial gauges and unused slack follow Dirichlet(a,b,1), giving volume a!b!/(a+b)! and for multiindex alpha the multiplier (a+1)_{|alpha_A|}(b+1)_{|alpha_B|}/(a+b+1)_{|alpha|}. This yields all-degree exact rational moments by cotree induction. The pairwise moment ratio R at a join has crossing value (N+1)/(N+2) and within-factor multiplier (a+2)/(a+1)*(N+1)/(N+2)>1, propagating edge R≤(n+1)/(n+2), nonedge R≥1 with strictness precisely for nonedges in connected components. Independently integrated the P4 stable-set polytope: normalization 5/24, E x2=7/25, E x2x3=1/15 and endpoint nonedge covariance -11/3750. The known forbidden induced P4 characterization then proves the hereditary iff; finite checks do not replace the Dirichlet proof.

## originality

PASS

The published multipartite stable-set theorem is a proper special case of the cotree formula, but cannot imply the all-alternating-cotree recurrence and induced-P4 hereditary characterization without additional arguments. General stable-set-polytope and moment-variety papers supply background/algorithms, not the graph-specific sharp covariance sign iff. The universal Dirichlet-free-sum method is structurally motivated and its specialized consequences survive known coverage.

## value

PASS

A natural hierarchical graph class yields every uniform-volume mixed moment by a short cotree recursion, plus a sharp graph-recovery signature using covariance signs and a forbidden-subgraph boundary. The hereditary sign characterization is a structural all-cograph theorem, not a textbook consequence of the known multipartite special case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
