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

Both products begin with their left word; equality forces prefix comparability, which conversely gives commutation. For the resulting strict ancestor graph, the level-constant restriction has one ancestor per earlier level and the stated factorial number of descendants per later level. For a vertex with k+1 children, weights orthogonal to the all-ones vector on children cancel the adjacency contribution at the vertex itself and all its ancestors, while each child's radial coordinates act by H_k. Nested contrast spaces are orthogonal by levelwise cancellation; disjoint subtrees are orthogonal by support. Completeness can be checked at each absolute depth j: if N_d=n!/(n−d)!, the dimensions at that depth add to 1+Σ_{d<j}N_d(n−d−1)=1+Σ_{d<j}(N_{d+1}−N_d)=N_j. The restrictions are self-adjoint in the positive weights k!/(k−i)! on the levels. For M=H_k+I the last two rows and columns coincide. In the leading k-square minor, differencing successive rows produces pivots k−1 through 1 and a last first-column entry 1, hence determinant (−1)^(k−1)(k−1)!. All principal cofactors vanish except the two equal ones at the endpoints of the identical pair. This gives P'_k(−1)=−2(k−1)! and telescoping exponents give n!. The k=1 minor is [1]. For n≥2 the empty word alone is central; deleting it partitions the graph by first letter into n copies of the smaller graph.

## originality

PASS

The supported distinct contribution is the explicit orthogonal adjacency decomposition into depthwise sibling modes with identified factorial-sized quotient entries and block multiplicities, and the simple-root derivative for each radial block. The prefix graph itself occurs in older work; the bulk characteristic polynomial is recoverable algebraically from a prior trivially perfect graph recursion, and the whole-graph −1 count is covered by general cograph multiplicity results. Neither bare spectral computability nor the whole-graph −1 count is independent novelty.

## value

PASS

The orthogonal block spaces identify actual adjacency modes, not only a factorization or an eigenvalue count. They give a constructive eigenfunction reduction from a graph with factorially many vertices to depth quotients of size at most n+1 and locate each copy at a specific prefix with levelwise cancellation. This is useful for adjacency representation and eigenfunction questions where a characteristic polynomial or a congruence algorithm cannot recover the modes. The analysis of −1 within each radial block further identifies how that repeated eigenvalue is assembled.

The dated certificate retains the supplied scientific assessment, sources and limitations.
