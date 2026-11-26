# Independent mathematical audit

## correctness

PASS

For the matching-deleted K5,5 (not a five-cycle), four vertices on one shore are disconnected (10); a 3+1 split is disconnected exactly when the minority index occurs in the majority (60); a 2+2 split is disconnected exactly when both diagonal pairs are absent, leaving two disjoint edges (10). Thus all 80 complementary six-sets are distinct facets. Membership in the cut complex is equivalent to being disjoint from a disconnected quartet, so the Alexander dual consists of sets containing no disconnected quartet. I independently generated both complexes by bit masks with an induced reachability test and constructed and topologically sorted the complete oriented nonempty-face Hasse graphs. With the two shores swapped in the pivot order, the original had f=(10,45,120,210,232,80), 697 faces, 335 matches, 2930 oriented covers, and critical counts {0:1,4:26}; the dual had f=(10,45,120,130,20), 325 faces, 149 matches, 1070 oriented covers, and critical counts {0:1,3:26}. All vertices of both directed graphs were sorted, establishing acyclicity rather than just computing counts. The discrete Morse CW theorem gives one vertex and 26 cells of dimension 4 (respectively 3), attached to a point. This proves the two full wedges and consequently the free integral homology in the stated degrees. Pure shellability of the original pure 5-complex would give zero reduced H4, so it is not shellable. Replay: python3 /workspace/reproduce_reviews.py 5.

## originality

PASS

Exact ordinary four-cut homotopy of the ten-vertex crown and its dual is distinct from the closest inspected statements. In particular, the primary clique-prism theorem concerns the graph complement, not the Alexander dual, and the strongest nearby indexed four-cut computations are for the eight-vertex and twelve-vertex crowns. The six-crown record references a five-crown one-degree calculation without separately proving or tabulating this homotopy type. No priority order follows from same-day labels.

## value

PASS

The first crown larger than the cube is a natural next instance at the same cut parameter. The exact homotopy type of both complexes, rather than just Betti counts, gives a pure nonshellable five-complex and distinguishes this order from both the cube and the adjacent six-crown's mixed-degree behavior. The case is useful as a concrete comparison point for graph-order and cut-parameter classification, without claiming an all-order formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
