---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

The uniform recurrent sandpile addition map permutes states, so E[toppling vector]=L^{-1}e_r exactly. On a sink-rooted tree the grounded Green kernel is depth(LCA(u,v)), and because r is the sink-adjacent source leaf, L^{-1}e_r=e_r. For a new edge r-x at distance d from sink with descendant sizes q_i, Sherman-Morrison with b=e_r-e_x gives E X=1+(sum_{i=1}^d q_i-1)/(d+2). Every q_i<=N-i+1; a path achieves all bounds. The discrete difference F_N(d+1)-F_N(d)=2(N+2)/((d+2)(d+3))-1/2 yields the exact smallest maximizing chord and the asymptotic N+7/2-2sqrt(N+2)+O(N^-1/2). If the edge avoids r the mean remains 1. Independent rational grounded-Laplacian enumeration checked all missing edges for all labeled source-leaf trees with N<=3. Universal extremality is from the inequality and equality construction, not enumerations.

## originality

PASS

PASS best-of-knowledge: earlier sandpile works establish uniform recurrent addition, Green-function expected topplings, tree avalanche polynomials and block-cut cycle formulas. These antecedents do not give the all-tree/all-one-edge-sharp extremum with a sink-adjacent source leaf, the optimal square-root chord depth, or the asymptotic deficit. Resultary search located a different Braess-type chord perturbation on cycles, whose base graphs are not trees; neither its sign law nor its ratio bound directly imply the tree optimization.

## value

PASS

PASS: this is a natural and broad extremal graph perturbation question, and changing a single edge raises a stationary expectation from exactly 1 to order N. The path extremizer and sqrt(N) optimal chord depth are precise structural features; the theorem supplies a sharp bound on expectation for any finite rooted source-leaf tree, independently useful to sandpile and electrical-network perturbation studies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
