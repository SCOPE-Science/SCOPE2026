# Independent mathematical audit

## correctness

PASS

Every mixed induced subgraph of the intact graph is connected. On a mixed set containing u and v, a vertex in any third part keeps the graph connected after deletion; with just the first two parts present and at least two vertices in each, an alternate length-three path also keeps it connected. In the remaining cases deleting uv isolates the endpoint alone in its part. Thus the only new faces are the listed sets of size r+1, exactly t_r in number. Each has an explicit mixed r-set facet with just that one proper coface: it omits the endpoint in the shore with the additional vertices, and cannot lie in a pure-part coface or in a second new face. The word 'unique' in Step 2 need not mean that a new simplex has no other free facet (a newly allowed triangle on the whole vertex set can have three); the required and used property is uniqueness of the coface of the chosen facet. These collapses followed by anchoring the pure parts leave dimension at most r−1. Both originals contain the full (r−1)-skeleton, giving (r−2)-connectivity; the dimension bound yields wedges by the connected-graph case or Hurewicz and Whitehead. For the intact complex the collapse from the skeleton count removes exactly C(m_i−1,r) faces of dimension r−1 in each part. The modified complex removes t_r additional such faces, giving the stated rank by Pascal's identity. The relative chain complex has only the t_r new r-simplices, so the reduced long exact sequence gives a short exact sequence of free abelian groups in the claimed degrees; freeness of the target yields the integral splitting and primitivity. For r≥N the complexes are simplices and all binomial ranks are zero. This verifies the map, not just the two ranks.

## originality

PASS

The intact ranks and wedge theorem are prior; no originality is assigned to them or to the cited bipartite r=2 baseline. The all-r one-edge comparison for arbitrary multipartitions and its kernel on integral homology survive the closest checked comparisons. In particular the nearest matching-defect persistence record uses a different complex.

## value

PASS

For a natural family the theorem precisely quantifies the topology killed by one local edit across all thresholds, and identifies an integral split quotient rather than merely giving Betti numbers before and after. The classification of changed faces and the integral ranks make this a useful test case for persistence under graph edits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
